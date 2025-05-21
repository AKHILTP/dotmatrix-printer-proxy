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

## 📦 Prerequisites

- Python 3.7.3 (for Odoo 14) or Python 3.8.20 (for Odoo 15+)
- Add Python to your system PATH during installation
- `pip` installed for managing Python packages

---

## 📁 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AKHILTP/dotmatrix-printer-proxy
cd dotmatrix-printer-proxy

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

