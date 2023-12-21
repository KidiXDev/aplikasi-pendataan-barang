from tkinter import messagebox
import mysql.connector

class dbConfig:
    def db():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="app_pendataan"
            )
        except Exception as e:
            messagebox.showinfo("Connection error", e)
            return