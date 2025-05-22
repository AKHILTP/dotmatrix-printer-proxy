from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import platform
import subprocess

import logging
# Try importing Windows-only modules
# Optional: Uncomment if using Windows printer API
# try:
#     import win32api
#     import win32print
# except ImportError:
#     win32api = None
#     win32print = None

_logger = logging.getLogger(__name__)


app = Flask(__name__)
CORS(app)

TEMPPRINT_FILE = 'tempprint.txt'

"""use encoding='utf-8' instead 'us-ascii' to support characters from all world languages"""
def create_default_files():
    """Ensure required files exist"""
    if not os.path.exists(TEMPPRINT_FILE):
        with open(TEMPPRINT_FILE, 'w', encoding='utf-8') as fp:
            pass

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
            # if not win32api or not win32print:
            #     return jsonify({'status': 'error', 'message': 'pywin32 not available on this system'}), 500
            # printer_name = win32print.GetDefaultPrinter()
            # _logger.info(f"Using printer: {printer_name}")

            # # Print using Windows ShellExecute
            # win32api.ShellExecute(
            #     0,
            #     "print",
            #     TEMPPRINT_FILE,
            #     None,
            #     ".",
            #     0
            # )
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


if __name__ == '__main__':
    create_default_files()
    # Run Flask's built-in dev server on port 8000
    app.run(host='127.0.0.1', port=8000, debug=True)


# @app.route('/dotmatrix/print', methods=['POST'])
# def dotmatrix_print():
#     printer_data = request.form['printer_data']
#     log_file = open(TEMPPRINT_FILE, 'w', encoding="us-ascii")  # pylint: disable=consider-using-with
#     log_file.write(printer_data)
#     log_file.write('\n')  # ASCII with line terminator
#     log_file.close()
#     os.startfile(TEMPPRINT_FILE, "print")
    
#     # p = win32print.OpenPrinter(PRINTER_NAME)
#     #
#     #
#     # job = win32print.StartDocPrinter(p,1,("DOTMATRIX",None,"RAW"))
#     # win32print.StartPagePrinter(p)
#     # win32print.WritePrinter(p,printer_data.encode() )
#     # win32print.EndPagePrinter(p)
#     # win32print.EndDocPrinter(p)
#     # win32print.ClosePrinter(p)
    