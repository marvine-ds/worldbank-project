import mysql.connector
from config import DB_CONFIG


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def test_connection():
    try:
        conn = get_connection()
        print("✅ MySQL connection successful!")
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)


