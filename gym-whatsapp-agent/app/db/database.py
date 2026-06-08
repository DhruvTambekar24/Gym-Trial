import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "data.sqlite"

def get_conn():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn
