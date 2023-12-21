import mysql.connector
from models import config
from tkinter import messagebox
from str_basic_encryption import StrEncryption

class LoginFormViewModel:
    def __init__(self):
        self.db = config.dbConfig.db() # inisialisasi database

    def loginAction(self, username, password, ins):
        dbc = self.db.cursor()
        encryptor = StrEncryption()
        encrypted_password = encryptor.str2md5(password) # mengenkripsi password menjadi md5 hash
        
        # query mysql untuk mencari username dan password yang sama
        query = "SELECT * FROM account WHERE username = %s AND password = %s"

        try:
            dbc.execute(query, (username, encrypted_password)) # menjalankan perintah mysql
            result = dbc.fetchone() # menyimpan hasil

            if result:
                print("Login successful")
                ins.loadMainMenu() # jika login berhasil lanjutkan ke main menu
            else:
                messagebox.showinfo("Error", "Invalid username or password") # jika login gagal munculkan pop up username atau password salah
                print("Login failed")
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", err) # tampilkan pop up error jika terjadi kesalahan
        finally:
            dbc.close() # menutup koneksi database
