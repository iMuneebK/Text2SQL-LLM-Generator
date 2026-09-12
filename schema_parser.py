import sqlite3

def get_schema(db_path="database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    schemas = cursor.fetchall()
    conn.close()
    return "\n".join([s[0] for s in schemas if s[0]])
