# 🖨️ Printer Proxy (Dotmatrix + Thermal)

A lightweight **Flask-based API service** to send raw text/img directly to a Dotmatrix Printer from **Odoo (v14/v15+)** or any system via HTTP requests.  
Supports **Windows, Linux, and macOS** 🪟🐧🍎

![Dotmatrix Printer Proxy](https://img.shields.io/badge/Dotmatrix-Printer%20Proxy-blueviolet?style=for-the-badge&logo=print)
![CUPS Enabled](https://img.shields.io/badge/CUPS-Enabled-orange?style=for-the-badge&logo=linux)
![Odoo Ready](https://img.shields.io/badge/Odoo-Ready-purple?style=for-the-badge&logo=odoo)
![Flask API](https://img.shields.io/badge/Flask-API-success?style=for-the-badge&logo=flask)
![Cross Platform](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge&logo=windows)
![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## Supports:
- 🧾 Dotmatrix printers (RAW text)
- 🔥 Thermal printers (PDF)

## 🚀 Features

- ✅ Simple API to receive and print data  
- 🧾 Compatible with **Odoo v14 (Python 3.7.3)** and **v15+ (Python 3.8.20)**  
- 🌍 Cross-platform support (**Windows, Linux, macOS**)  
- 🔒 CORS enabled (accessible from browsers or Odoo)  
- 🛠️ Easily extendable for network printers or direct printer APIs  
- Single proxy for multiple printer types
- POS-style auto printing

---

## 📸 Screenshots / Demo

- Printer Proxy in action  
![Printer Proxy Demo](assets/dot_matrix_1.png)

---


## 📥 Installation

### 📌 Clone/Download

1. url :-https://github.com/AKHILTP/dotmatrix-printer-proxy

git clone https://github.com/AKHILTP/dotmatrix-printer-proxy

2. download the ZIP and extract to:

C:/ in Windows

~/home/ in Linux/Ubuntu

## 🟦 Windows Setup Instructions

#If Python is not installed:

1. Download Python 3.8.20 from the official website or run the provided installer.
2. **Ensure you add Python to your system PATH during installation.**

or

- Alternatively, run `install_python.bat` by double-clicking it. This will install Python 3.8.20 silently and add it to your PATH.

#After installation, open a CMD and verify with:

command: python3 --version

## 🟦 Steps

1.  **OPen CMD: open path to file final path of folder**
      eg: cd dotmatrix-printer-proxy

2. **Create & Activate a Virtual Environment**:

   - python -m venv venv
   - venv\Scripts\activate


3. **Install Required Packages**:

   <!-- wsl --install
   sudo apt update
   sudo apt install -y python3-full python3-venv poppler-utils

   ** FOr go to local disc cpath.
   📂 Windows C: drive path in WSL 
   command :- cd /mnt/c
   cd <path of the proxy folder> open
   then.
   python3 -m venv venv
   source venv/bin/activate
   
   <!-- sudo apt install -y python3-pip libcups2-dev cups -->
   <!-- pip3 install pycups

   in window cmd prompt. --> 

   - pip install -r requirements.txt
   - python -m pip install --upgrade pip 
      (if raise: not upgraded pip warning)

4. **For thermal print to support image file**:
   
   - pip install pywin32 python-escpos
   - pip install python-escpos pillow pdf2image pyusb
   <!-- - brew install poppler -->

5. **Start the Flask Application**:

      * Double-click on `start.bat` in the proxy folder.
      for shortcut for easy running can add to desktop
      * **Do not close the CMD terminal** as it keeps the server running.

---------------

## 🟦 Linux Setup Instructions

1.  **OPen CMD: open path to file final path of folder**
      eg: cd dotmatrix-printer-proxy

2. **Make the installation script- run it**:

   - chmod +x install_python.sh
   - ./install_python.sh

3. **Create & Activate a Virtual Environment**:

   - python3 -m venv venv
   - source venv/bin/activate

4. **Install Required Packages**:

   - pip install -r requirements.txt
   - pip install python-escpos


5. **Ensure CUPS is Installed and Printer is Not Paused**:

   - sudo apt install cups

   * Make sure:

     * The `lp` command is installed.
     * The printer is configured and not paused.

6. **For thermal print to support image file**:
   
   - sudo apt install cups poppler-utils

7. **Start the Flask Application**:

   - chmod +x start.sh
   - ./start.sh
--------------

For developer using this Printer for Dotmatrix
## 🛠️ API Usage

* **Endpoint:** `http://localhost:8000/dotmatrix/print`

* **Method:** `POST`

* **Headers:** `Content-Type: application/json`

* **Body:**
POST /dotmatrix/print

  json
  {
    "printer_data": "Your raw text data to print"
  }


For developer using this Printer for thermal


POST /thermal/print
json
{
  "pdf_base64": "<base64_pdf>",
  "paper_width": 80
}



## 📬 Support

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/AKHILTP/dotmatrix-printer-proxy/issues).