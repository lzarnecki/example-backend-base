#!/usr/bin/env bash

apt-get install virtualenv

# Python
virtualenv -p python3 venv
source venv/bin/activate
python -V
pip install -r requirements.txt