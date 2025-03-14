#!/bin/bash

install_python() {
    if command -v python3 &>/dev/null; then
        echo "Python3 is already installed."
    else
        echo "Installing Python3..."
        sudo apt update && sudo apt install -y python3 python3-pip
    fi
}

install_python
PYTHON_PATH=$(which python3)
echo "Python path: $PYTHON_PATH"
$PYTHON_PATH ReleaseScript.py