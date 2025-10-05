#!/bin/bash

export SQLITE_DB_PATH='/home/nipunsood42/local.db'
rm -rf venv
python3 -m venv venv
./venv/bin/activate
pip install -r server/requirements.txt -t ./venv
pip install gunicorn -t ./venv
gunicorn -w 2 'server:app'