# 🖨️ Dotmatrix Printer Proxy API

A lightweight Flask-based API service to send raw text data directly to a Printer from Odoo (v14 or v15+), or any system via a simple HTTP request. Supports both Windows and Linux environments.

## 🚀 Features

* ✅ Simple API to receive and print data
* 🧾 Compatible with **Odoo v14** (Python 3.7.3) and **v15+** (Python 3.8.20)
* 🪟 Supports **Windows **Linux **Mac `**
* 🔒 CORS enabled (API accessible from browsers or Odoo)
* 🛠️ Easily extendable for network printers or direct printer APIs


## 🟦 Windows Setup Instructions

### 📦 Prerequisites: Installing Python

#If Python is not installed:

1. Download Python 3.8.20 from the official website or run the provided installer.
2. **Ensure you add Python to your system PATH during installation.**

or

Alternatively, run `install_python.bat` by double-clicking it. This will install Python 3.8.20 silently and add it to your PATH.

#After installation, open a new CMD and verify with:

python --version


### 📁 Setup Steps

1. **Clone/download the Repository zip**:
   -  url :-https://github.com/AKHILTP/dotmatrix-printer-proxy

   -  CMD: open path to file
      eg: cd dotmatrix-printer-proxy


2. **Create & Activate a Virtual Environment**:

   - python -m venv venv
   - env\Scripts\activate

3. **Install Required Packages**:

   - pip install -r requirements.txt

4. **Start the Flask Application**:

      * Double-click on `start.bat` in the proxy folder.
      * **Do not close the CMD terminal** as it keeps the server running.

---------------

## 🟦 Linux Setup Instructions

### 📦 Prerequisites: Installing Python and Dependencies

1. **Make the installation script- run it**:

   - chmod +x install_python.sh
   - ./install_python.sh

2. **Create & Activate a Virtual Environment**:

   - python3 -m venv venv
   - source venv/bin/activate

3. **Install Required Packages**:

   - pip install -r requirements.txt


4. **Ensure CUPS is Installed and Printer is Not Paused**:

   - sudo apt install cups

   * Make sure:

     * The `lp` command is installed.
     * The printer is configured and not paused.

5. **Start the Flask Application**:

   - chmod +x start.sh
   - ./start.sh
--------------
## 🛠️ API Usage

* **Endpoint:** `http://localhost:8000/dotmatrix/print`

* **Method:** `POST`

* **Headers:** `Content-Type: application/json`

* **Body:**

  json
  {
    "printer_data": "Your raw text data to print"
  }

## 📬 Support

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/AKHILTP/dotmatrix-printer-proxy/issues).