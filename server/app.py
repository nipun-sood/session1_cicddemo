from flask import Flask
from .logic import get_last_names_logic
from .dao import get_connection

app = Flask(__name__)
print("Flask app created.")

# Single persistent connection
db_conn = None

def init_db_connection():
    global db_conn
    db_conn = get_connection()

@app.route('/name/<fname>', methods=['GET'])
def get_api(fname):
    # Use logic.py to get last names by first name
    last_names = get_last_names_logic(db_conn, fname)
    return '<br>'.join(last_names), 200

init_db_connection()
if db_conn is None:
    raise Exception("Database connection could not be established.")
print("Database connection established.")
print("API endpoint /name/<fname> is set up.")