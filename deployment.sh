#!/bin/bash

export SQLITE_DB_PATH='/home/nipunsood42/local.db'
sqlite3 $SQLITE_DB_PATH < db/create_people_table.sql
rm -rf venv
python3 -m venv venv
. venv/bin/activate
pip install -r server/requirements.txt
pip install gunicorn
nohup gunicorn -w 2 -b 0.0.0.0 'server.app:app' > gn.log &