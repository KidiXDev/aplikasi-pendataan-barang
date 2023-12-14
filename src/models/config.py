import mysql.connector

class dbConfig:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="app_pendataan"
    )