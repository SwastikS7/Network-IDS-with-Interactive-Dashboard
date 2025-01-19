import sqlite3
from config import Config


def setup_database():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()

    # Create alerts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alerts (
        timestamp TEXT,
        source_ip TEXT,
        alert_type TEXT,
        details TEXT
    )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!")


if __name__ == "__main__":
    setup_database()