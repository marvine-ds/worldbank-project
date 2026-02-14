import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def insert_data(records):
    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO world_bank_indicators (
        country_code,
        country_name,
        year,
        indicator_code,
        indicator_name,
        value,
        is_aggregate
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        value = VALUES(value),
        country_name = VALUES(country_name),
        indicator_name = VALUES(indicator_name),
        is_aggregate = VALUES(is_aggregate);
    """

    cursor.executemany(insert_query, records)
    connection.commit()

    print(f"{cursor.rowcount} rows inserted/updated.")

    cursor.close()
    connection.close()
