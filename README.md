# 🖨️ Dotmatrix Printer Proxy API

A lightweight Flask-based API service to send raw text data directly to a Dot Matrix Printer from Odoo (v14 or v15+), or any system via a simple HTTP request. Supports both Windows and Linux environments.
---

## 🚀 Features

- ✅ Simple API to receive and print data
- 🧾 Compatible with **Odoo v14** (Python 3.7.3) and **v15+** (Python 3.8.20)
- 🪟 Supports **Windows `os.startfile()`** printing
- 🐧 Linux-friendly via `start.sh`
- 🔒 CORS enabled (API accessible from browsers or Odoo)
- 📁 Print content saved in `tempprint.txt` before printing
- 🛠️ Easily extendable for network printers or direct printer APIs

---
### 📦 Prerequisites Installing Python (Windows)

If Python is not installed:
- Python 3.7.3 (for Odoo 14) or Python 3.8.20 (for Odoo 15+)
- Add Python to your system PATH during installation

- Run `install_python.bat` by double-clicking it.
- This will install Python 3.8.20 silently and add it to your PATH.
- After installation, open a new CMD and verify with:

```bash
python --version


### 📦 Installing Python and dependencies(Linux)

Run the following commands in the terminal:

```bash
chmod +x install_python.sh
./install_python.sh

After this, you can create and activate a virtual environment, and install your Python requirements:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

## 📁 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/AKHILTP/dotmatrix-printer-proxy
cd git/dotmatrix-printer-proxy

#Create & Activate a Virtual Environmen
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate

# Install Required Packages
pip install -r requirements.txt

# On Windows:
start.bat
Double click on the start.bat in proxy file
Do not close the CMD terminal

# On LInux:
chmod +x start.sh
./start.sh

