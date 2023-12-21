import mysql.connector
from models import config
from tkinter import messagebox
from str_basic_encryption import StrEncryption

class LoginFormViewModel:
    def __init__(self):
        self.db = config.dbConfig.db()

    def loginAction(self, username, password, ins):
        dbc = self.db.cursor()
        encryptor = StrEncryption()
        encrypted_password = encryptor.str2md5(password)

        query = "SELECT * FROM account WHERE username = %s AND password = %s"

        try:
            dbc.execute(query, (username, encrypted_password))
            result = dbc.fetchone()

            if result:
                print("Login successful")
                ins.loadMainMenu()
            else:
                messagebox.showinfo("Error", "Invalid username or password")
                print("Login failed")
        except mysql.connector.Error as err:
            print(f"Error: {err}") 
        finally:
            dbc.close()
