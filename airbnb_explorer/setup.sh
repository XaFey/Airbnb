#!/bin/bash/
cd airbnb_explorer
set -e

echo " Virtual environment setup script for midterm project"
python -m venv .venv
source .venv/bin/activate

echo "Installing dependencies from requirements.txt"
pip install -r requirements.txt

echo "Setup complete! Thanks!"