#!/bin/bash

# Update the package lists for the repositories
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install build-essential and other required libraries
echo "Installing essential build tools..."
sudo apt install -y build-essential

# Install libraries for Python development
echo "Installing Python development libraries..."
sudo apt install -y libssl-dev libffi-dev python3-dev

# Install additional dependencies for Python
echo "Installing additional dependencies..."
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

# Add the deadsnakes PPA repository for newer Python versions
echo "Adding deadsnakes PPA repository..."
sudo add-apt-repository ppa:deadsnakes/ppa

# Update the package lists again after adding the repository
echo "Updating package lists again..."
sudo apt update

# Install Python 3.10
echo "Installing Python 3.10..."
sudo apt install -y python3.10

# Install distutils for Python 3.10 (for pip installation)
echo "Installing Python 3.10 distutils..."
sudo apt install -y python3.10-distutils

# Download and install pip for Python 3.10
echo "Downloading and installing pip..."
wget https://bootstrap.pypa.io/get-pip.py
python3.10 get-pip.py


# Clean up the downloaded get-pip.py file
echo "Cleaning up..."
rm get-pip.py


echo "Installing python3.10-venv"
sudo apt install python3.10-venv

# Create a virtual environment
echo "Creating a virtual environment..."
python3.10 -m venv env

echo "Activating env"
source env/bin/activate

echo "Python 3.10 and pip installation complete. Virtual environment activated."
