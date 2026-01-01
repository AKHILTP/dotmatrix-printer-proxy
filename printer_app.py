from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import platform
import subprocess
import logging
import base64

from escpos.printer import Usb, Network
from pdf2image import convert_from_path
from PIL import Image

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

TEMPPRINT_FILE = "tempprint.txt"
TEMP_PDF = "temp_thermal.pdf"

# ------------------------------------------------
# FILE PATHS
# ------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")

TEMPPRINT_FILE = os.path.join(TEMP_DIR, "tempprint.txt")
TEMP_PDF = os.path.join(TEMP_DIR, "temp_thermal.pdf")

"""use encoding='utf-8' instead 'us-ascii' to support characters from all world languages"""
# def create_default_files():
#     """Ensure required files exist"""
#     if not os.path.exists(TEMPPRINT_FILE):
#         with open(TEMPPRINT_FILE, 'w', encoding='utf-8') as fp:
#             pass     


# ------------------------------------------------
# INIT (IMPORTANT FOR WAITRESS)
# ------------------------------------------------
def init_files():
    os.makedirs(TEMP_DIR, exist_ok=True)

    if not os.path.exists(TEMPPRINT_FILE):
        with open(TEMPPRINT_FILE, "w", encoding="utf-8"):
            pass

init_files()  

# ------------------------------------------------
# DOTMATRIX PRINT — KEEP FULL LOGIC HERE ✅
# ------------------------------------------------
@app.route('/dotmatrix/print', methods=['POST'])
def dotmatrix_print():
    try:
        # Try JSON first
        if request.is_json:
            data = request.get_json()
            printer_data = data.get('printer_data')
        else:
            # Fallback to form data
            printer_data = request.form.get('printer_data')
        
        if not printer_data:
            return jsonify({'status': 'error', 'message': 'Missing printer_data'}), 400

        # Save data to file
        with open(TEMPPRINT_FILE, 'w', encoding='utf-8') as log_file:
            log_file.write(printer_data + '\n')

        # Detect OS and print accordingly
        system_os = platform.system()
        _logger.info(
            "system_os %s" % (system_os)
        )
        if system_os == "Windows":
            os.startfile(TEMPPRINT_FILE, "print")
            
        else:
            # Linux/macOS: Use lp or lpr
            try:
                subprocess.run(["lp", TEMPPRINT_FILE], check=True)
            except Exception as linux_error:
                # Try with lpr if lp fails
                subprocess.run(["lpr", TEMPPRINT_FILE], check=True)

        return jsonify({'status': 'OK'})
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# ==============================================================
# THERMAL PRINT (PDF → IMAGE → ESC/POS)
# ==============================================================
@app.route("/thermal/print", methods=["POST"])
def thermal_print():
    try:
        data = request.get_json() or {}

        pdf_base64 = data.get("pdf_base64")
        printer_type = data.get("printer_type", "usb").lower()
        paper_width = int(data.get("paper_width", 80))

        if not pdf_base64:
            return jsonify({
                "status": "error",
                "message": "Missing pdf_base64"
            }), 400

        # ------------------------------------------------
        # Decode PDF
        # ------------------------------------------------
        # pdf_bytes = base64.b64decode(pdf_base64)
        if isinstance(pdf_base64, str):
            pdf_base64 = pdf_base64.encode("utf-8")

        pdf_bytes = base64.b64decode(pdf_base64)
        with open(TEMP_PDF, "wb") as f:
            f.write(pdf_bytes)

        # ------------------------------------------------
        # Convert PDF → Images
        # ------------------------------------------------
        images = convert_from_path(TEMP_PDF, dpi=203)

        max_width_px = 576 if paper_width == 80 else 384

        # ------------------------------------------------
        # Initialize Printer
        # ------------------------------------------------
        if printer_type == "usb":
            if not data.get("vendor_id") or not data.get("product_id"):
                return jsonify({
                    "status": "error",
                    "message": "Missing USB vendor_id / product_id"
                }), 400

            vendor_id = int(data["vendor_id"], 16)
            product_id = int(data["product_id"], 16)

            _logger.info(
                "Thermal USB printer VID=%s PID=%s",
                data["vendor_id"],
                data["product_id"]
            )

            printer = Usb(vendor_id, product_id)

        else:  # network
            if not data.get("ip"):
                return jsonify({
                    "status": "error",
                    "message": "Missing printer IP"
                }), 400

            ip = data["ip"]
            port = int(data.get("port", 9100))

            _logger.info(
                "Thermal Network printer %s:%s",
                ip, port
            )

            printer = Network(ip, port)

        # ------------------------------------------------
        # Print Images
        # ------------------------------------------------
        for img in images:
            img = img.convert("L")
            w, h = img.size

            if w > max_width_px:
                ratio = max_width_px / float(w)
                img = img.resize(
                    (max_width_px, int(h * ratio)),
                    Image.LANCZOS
                )

            printer.image(img)

        printer.cut()

        return jsonify({"status": "OK"})

    except Exception as e:
        _logger.exception("Thermal print failed")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
        
        
@app.route("/thermal/validate", methods=["POST"])
def thermal_validate():
    try:
        data = request.get_json() or {}

        printer_type = data.get("printer_type", "usb").lower()

        if printer_type not in ("usb", "network"):
            return jsonify({
                "valid": False,
                "message": "Invalid or missing printer_type"
            }), 400

        if printer_type == "usb":
            if not data.get("vendor_id") or not data.get("product_id"):
                return jsonify({
                    "valid": False,
                    "message": "USB printer requires vendor_id and product_id"
                }), 400

            # Validate hex format
            try:
                int(data["vendor_id"], 16)
                int(data["product_id"], 16)
            except ValueError:
                return jsonify({
                    "valid": False,
                    "message": "Invalid USB VID/PID format (use hex, e.g. 0x04b8)"
                }), 400

        if printer_type == "network":
            if not data.get("ip"):
                return jsonify({
                    "valid": False,
                    "message": "Network printer requires IP address"
                }), 400

        return jsonify({
            "valid": True,
            "message": "Thermal printer configuration is valid"
        })

    except Exception as e:
        _logger.exception("Thermal validation failed")
        return jsonify({
            "valid": False,
            "message": str(e)
        }), 500



# ==============================================================
# MAIN
# ==============================================================
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)


# if __name__ == '__main__':
#     create_default_files()
#     # Run Flask's built-in dev server on port 8000
#     app.run(host='127.0.0.1', port=8000, debug=True)
    
        