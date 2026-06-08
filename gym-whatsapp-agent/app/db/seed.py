from app.db.database import get_conn
from app.db.models import create_tables

def seed():
    conn = get_conn()
    create_tables(conn)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO members (id,name,phone) VALUES (?,?,?)", ("member_123","Test User","+1000000000"))
    conn.commit()
    conn.close()
