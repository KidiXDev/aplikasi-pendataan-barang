import mysql.connector
from models import config
from tkinter import messagebox
from str_basic_encryption import StrEncryption

class LoginFormViewModel:
    def __init__(self):
        self.db = config.dbConfig.db()
        self.dbc = self.db.cursor()

    def loginAction(self, username, password, menu):
        encryptor = StrEncryption()
        encrypted_password = encryptor.str2md5(password)

        query = "SELECT * FROM account WHERE username = %s AND password = %s"

        try:
            self.dbc.execute(query, (username, encrypted_password))
            result = self.dbc.fetchone()

            if result:
                print("Login successful")
                menu.loadMainMenu()
            else:
                messagebox.showinfo("Error", "Invalid username or password")
                print("Login failed")
        except mysql.connector.Error as err:
            print(f"Error: {err}") 
        finally:
            self.dbc.close()
