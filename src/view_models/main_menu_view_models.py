from tkinter.ttk import Treeview
import mysql.connector
from mysql.connector import IntegrityError
from models import config
from tkinter import messagebox
import locale

class MainMenuViewModels:
    def __init__(self):
        self.db = config.dbConfig.db()
    
    def execute_query(self, query, values=None):
        cursor = self.db.cursor()
        try:
            if values:
                cursor.execute(query, values) 
            else:
                cursor.execute(query)
            self.db.commit()
            return True
        except IntegrityError as e:
            print(f"Error executing query: {e}")
            messagebox.showinfo("An error occured", f"{str(e)}")
            self.db.rollback()  # melakukan rollback karena terjadi exception...
            return False
        finally:
            cursor.close()

    def fetch_data(self):
        # fetch data dari database
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM data_barang")
        data = cursor.fetchall()
        cursor.close()
        return data

    def format_currency(self, value):
        # Proses mengubah format currency menjadi rupiah
        locale.setlocale(locale.LC_ALL, 'id_ID')  # id_ID = locale 4 Indonesia
        return locale.currency(value, grouping=True, symbol='Rp')

    def refresh_table(self, tree: Treeview):
        # Clear data di table yang udh ada
        for item in tree.get_children():
            tree.delete(item)

        # Fetch data dari database trs masukin ke table
        data = self.fetch_data()
        for row in data:
            # ubah format column ke 3 menjadi tampilan currency IDR
            formatted_row = row[:2] + (self.format_currency(row[2]),) + row[3:]
            tree.insert("", "end", values=formatted_row)

    def insert_data(self, tree, id_barang, nama_barang, harga, stok):
        # Mengecek apakah ada field kosong atau tidak
        if not all([id_barang, nama_barang, harga, stok]):
            messagebox.showinfo("An error occured", f"Field cannot be empty")
            return
        
        # if not all([isinstance(id_barang, int), isinstance(nama_barang, str), isinstance(harga, int), isinstance(stok, int)]):
        #     messagebox.showinfo("An error occured", f"Incorrect data value type")
        #     return
        
        # jika tidak lanjut masukkan data baru ke database
        print(f"ID: {id_barang} Nama: {nama_barang} Harga: {harga} Stok: {stok}")
        query = "INSERT INTO data_barang (id_barang, nama_barang, harga, stok) VALUES (%s, %s, %s, %s)"
        values = (id_barang, nama_barang, harga, stok)
        result = self.execute_query(query, values)
        self.refresh_table(tree)
        
        if result:
            messagebox.showinfo("Success!", "Data entered successfully")

    def update_data(self, tree, id_barang, nama_barang, harga, stok):
        # Implement your logic to get updated data from user input
        # Then update the corresponding row in the database
        selected_item = tree.selection()
        if selected_item:
            # Example: Updating the first column (ID Barang) with a new value
            query = "UPDATE data_barang SET id_barang = %s, nama_barang = %s, harga = %s, stok = %s WHERE id_barang = %s"
            values = (id_barang, nama_barang, harga, stok, tree.item(selected_item, "values")[0])
            result = self.execute_query(query, values)
            self.refresh_table(tree)
            
            if result:
                messagebox.showinfo("Success!", "Data edited successfully")
        else:
            messagebox.showinfo("Error", "Please select item first")
            
    def tree_on_double_click(self, tree, tfId, tfBarang, tfHarga, tfStok):
        selected_item = tree.selection()

        item_data = tree.item(selected_item, "values")

        tfId.delete(0, "end")
        tfId.insert(0, item_data[0])

        tfBarang.delete(0, "end")
        tfBarang.insert(0, item_data[1])
        
        # Menghapus karakter selain digit dan koma
        harga_str = ''.join(filter(lambda x: x.isdigit() or x == ',', item_data[2]))

        # Mengganti koma dengan string kosong
        harga_str = harga_str.replace(',', '')

        # Mengonversi ke bilangan bulat
        harga_int = int(harga_str)

        # Menghapus dua angka 0 terakhir
        price = int(harga_int / 100)

        tfHarga.delete(0, "end")
        tfHarga.insert(0, str(price))

        tfStok.delete(0, "end")
        tfStok.insert(0, item_data[3])
        

    def delete_data(self, tree):
        selected_item = tree.selection()
        if selected_item:
            # Fungsi untuk menghapus baris/row berdasarkan id barang yang dipilih
            result = messagebox.askokcancel("Confirmation", "Are you sure want to delete this item?")
            if result is True:
                query = "DELETE FROM data_barang WHERE id_barang = %s"
                value = tree.item(selected_item, "values")[0]
                self.execute_query(query, (value,))
                self.refresh_table(tree)
        else:
            messagebox.showinfo("Error", "Please select item first")
            
    def reset_entry(self, tfId, tfBarang, tfHarga, tfStok):
        tfId.delete(0, "end")
        tfBarang.delete(0, "end")
        tfHarga.delete(0, "end")
        tfStok.delete(0, "end")