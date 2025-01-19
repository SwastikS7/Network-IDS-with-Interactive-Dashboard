import sqlite3
from config import Config

def init_db():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS alerts
        (timestamp TEXT, source_ip TEXT, alert_type TEXT, details TEXT)
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()