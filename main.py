import psycopg
from dotenv import load_dotenv
import os

# Load variables from the .env
load_dotenv()

# Read variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", "5432")

# Build connection string
conn_str = f"dbname={DB_NAME} user={DB_USER} host={DB_HOST} port={DB_PORT} password={DB_PASSWORD}"

# Establish the connection
with psycopg.connect(conn_str) as connection:
    print("successful connection")

    # Use the connection and cursor inside the with block
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "any")
        )
        # Commit the transaction within the context
        connection.commit()

