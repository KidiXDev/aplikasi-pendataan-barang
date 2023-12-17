import mysql.connector
from models import config
from tkinter import messagebox

class MainMenuViewModels:
    def __init__(self):
        self.db = config.dbConfig.db
    
    def execute_query(self, query, values=None):
        cursor = self.db.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        self.db.commit()
        cursor.close()

    def fetch_data(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM data_barang")
        data = cursor.fetchall()
        cursor.close()
        return data

    def refresh_table(self):
        # Clear existing items in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the database and insert into the table
        data = self.fetch_data()
        for row in data:
            self.tree.insert("", "end", values=row)

    def insert_data(self):
        # Implement your logic to get data from user input
        # For example, using Entry widgets or a separate form
        # Then insert the data into the database
        query = "INSERT INTO data_barang (column1, column2, column3, column4) VALUES (%s, %s, %s, %s)"
        values = ("value1", "value2", "value3", "value4")
        self.execute_query(query, values)
        self.refresh_table()

    def update_data(self):
        # Implement your logic to get updated data from user input
        # Then update the corresponding row in the database
        selected_item = self.tree.selection()
        if selected_item:
            # Example: Updating the first column (ID Barang) with a new value
            new_value = "new_value"
            query = "UPDATE data_barang SET column1 = %s WHERE column1 = %s"
            values = (new_value, self.tree.item(selected_item, "values")[0])
            self.execute_query(query, values)
            self.refresh_table()

    def delete_data(self):
        # Implement your logic to confirm deletion and delete the selected row
        selected_item = self.tree.selection()
        if selected_item:
            # Example: Deleting the row where ID Barang matches the selected value
            query = "DELETE FROM data_barang WHERE column1 = %s"
            value = self.tree.item(selected_item, "values")[0]
            self.execute_query(query, (value,))
            self.refresh_table()