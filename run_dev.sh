#!/usr/bin/env bash

source venv/bin/activate
FLASK_APP=app.py FLASK_DEBUG=1 flask run --host=0.0.0.0