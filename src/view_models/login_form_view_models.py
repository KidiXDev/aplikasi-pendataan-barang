import hashlib
import mysql.connector
import sys
from models import config
from tkinter import messagebox

class LoginFormViewModel:
    def __init__(self):
        self.db = config.dbConfig.db()
        self.dbc = self.db.cursor()
            
    
    def md5_hash_string(self, password):
        md5_hash = hashlib.md5()
        md5_hash.update(password.encode('utf-8'))
        hashed_string = md5_hash.hexdigest()

        return hashed_string

    def loginAction(self, username, password, ins):
        encrypted_password = self.md5_hash_string(password)

        query = "SELECT * FROM account WHERE username = %s AND password = %s"

        try:
            self.dbc.execute(query, (username, encrypted_password))
            result = self.dbc.fetchone()

            if result:
                print("Login successful")
                ins.loadMainMenu()
            else:
                messagebox.showinfo("Error", "Invalid username or password")
                print("Login failed")
        except mysql.connector.Error as err:
            print(f"Error: {err}") 
        finally:
            self.dbc.close()
