from dotenv import load_dotenv
import psycopg
import os

class DbConnectorDataSet:
    def __init__(self):
        load_dotenv()
        conn = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        conn.execute("""
        CREATE TABLE IF NOT EXISTS raw_data ()
        """)
        conn.commit()


    def insert_new_values(self, features):
        print("hello")

