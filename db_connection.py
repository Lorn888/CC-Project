import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host_name = os.environ.get("postgres_host")
database_name = "coffee_cartel_db"
user_name = os.environ.get("postgres_user")
user_password = os.environ.get("postgres_pass")

def get_db_connection():
    connection = psycopg2.connect(
        host = host_name,
        database = database_name,
        user = user_name,
        password = user_password
    )
    return connection