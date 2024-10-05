import mariadb
import sys

DATABASE_URL = "mysql+mariadb://Admin:2929@localhost:3306/admi_pass"

def get_db_connection():
    try:
        conn = mariadb.connect(
            user="Admin",
            password="2929",
            host="localhost",
            port=3306,
            database="admi_pass"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
        