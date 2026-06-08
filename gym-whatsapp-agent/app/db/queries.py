def get_member_by_phone(conn, phone):
    cur = conn.cursor()
    cur.execute("SELECT * FROM members WHERE phone = ?", (phone,))
    return cur.fetchone()
