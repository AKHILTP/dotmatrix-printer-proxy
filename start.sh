

#!/bin/bash

# Activate the virtual environment
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Virtual environment not found, please create it first."
    exit 1
fi

echo "Starting Dotmatrix Printer Proxy..."
waitress-serve --port=8000 printer_app:app
