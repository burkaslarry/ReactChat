import pymysql
from os.path import join, dirname
import os
from dotenv import load_dotenv

# Load the environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")



timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db=MYSQL_DATABASE,
    host=MYSQL_HOST,
    password=MYSQL_PASSWORD,
    read_timeout=timeout,
    port=15043,
    user=MYSQL_USERNAME,
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()