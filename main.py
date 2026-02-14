import os
from dotenv import load_dotenv

load_dotenv()

print("HOST:", os.getenv("DB_HOST"))
print("USER:", os.getenv("DB_USER"))
print("PASS:", os.getenv("DB_PASSWORD"))

from load_to_mysql import test_connection

if __name__ == "__main__":
    test_connection()

