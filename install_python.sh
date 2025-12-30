#!/bin/bash

echo "Updating package lists..."
sudo apt-get update

echo "Installing Python 3 and pip..."
sudo apt-get install -y python3 python3-pip

echo "Installing virtualenv..."
sudo pip3 install virtualenv

echo "Python version:"
python3 --version

echo "pip version:"
pip3 --version

echo "Done."
