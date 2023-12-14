import hashlib
import mysql.connector
from models import config

class LoginFormViewModel:
    def __init__(self):
        self.dbc = config.dbConfig.db.cursor()
    
    def md5_hash_string(self, password):
        md5_hash = hashlib.md5()
        md5_hash.update(password.encode('utf-8'))
        hashed_string = md5_hash.hexdigest()

        return hashed_string

    def loginAction(self, username, password):
        self.dbc = config.dbConfig.db.cursor()
        
        encrypted_password = self.md5_hash_string(password)

        query = "SELECT * FROM account WHERE username = %s AND password = %s"

        try:
            self.dbc.execute(query, (username, encrypted_password))
            result = self.dbc.fetchone()

            if result:
                print("Login successful")
            else:
                print("Login failed")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.dbc.close()
