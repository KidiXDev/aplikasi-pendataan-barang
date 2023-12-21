from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, StringVar
from view_models import main_menu_view_models as mainMenuVM

class MainMenu:
    def __init__(self):
        self.mainMenuViewModels = mainMenuVM.MainMenuViewModels()
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\frame1")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.window = Tk()

        self.window.title("Aplikasi Pendataan")
        self.window.geometry("1280x720")
        self.window.configure(bg = "#282727")
        self.window.iconbitmap(OUTPUT_PATH / Path(r"..\assets\icon.ico"))

        self.canvas = Canvas(
            self.window,
            bg = "#282727",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            22.0,
            117.0,
            782.0,
            703.0,
            fill="#D9D9D9",
            outline="")
        
        # Create Table
        columns = ("ID Barang", "Nama Barang", "Harga", "Stok")
        self.tree = ttk.Treeview(self.canvas, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)  # Adjust the width as needed

        # Insert sample data (you can replace this with your actual data)
        # TODO: Implement read items from database
        self.mainMenuViewModels.refresh_table(self.tree)

        # Place the table at the specified location
        self.tree.place(x=22, y=117, width=760, height=586)

        self.canvas.create_text(
            22.0,
            25.0,
            anchor="nw",
            text="Data Barang",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 40 * -1)
        )

        self.canvas.create_rectangle(
            22.0,
            76.0,
            265.0, 
            83.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            791.0,
            575.0,
            1268.0,
            709.0,
            fill="#282828",
            outline="")

        self.canvas.create_rectangle(
            799.0,
            584.0,
            1258.0,
            703.0,
            fill="#838383",
            outline="")

        self.canvas.create_text(
            858.0,
            604.0,
            anchor="nw",
            text="Total Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 16 * -1)
        )

        self.canvas.create_text(
            818.0,
            634.0,
            anchor="nw",
            text="Total Stok Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 16 * -1)
        )

        self.canvas.create_text(
            818.0,
            664.0,
            anchor="nw",
            text="Terakhir Diupdate:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 16 * -1)
        )

        btnDeleteImg = PhotoImage(
            file=relative_to_assets("button_1.png"))
        btnDelete = Button(
            image=btnDeleteImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mainMenuViewModels.delete_data(self.tree),
            relief="flat"
        )
        btnDelete.place(
            x=976.0,
            y=288.0,
            width=106.0,
            height=54.0
        )

        btnAddImage = PhotoImage(
            file=relative_to_assets("button_2.png"))
        btnAdd = Button(
            image=btnAddImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.mainMenuViewModels.insert_data(self.tree, tfIdBarang.get(), tfNamaBarang.get(), tfHargaBarang.get(), tfStokBarang.get()), self.mainMenuViewModels.reset_entry(tfIdBarang, tfNamaBarang,tfHargaBarang, tfStokBarang)),
            relief="flat"
        )
        btnAdd.place(
            x=855.0,
            y=288.0,
            width=108.0,
            height=57.0
        )

        btnEditImage = PhotoImage(
            file=relative_to_assets("button_3.png"))
        btbEdit = Button(
            image=btnEditImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.mainMenuViewModels.update_data(self.tree, tfIdBarang.get(), tfNamaBarang.get(), tfHargaBarang.get(), tfStokBarang.get()), self.mainMenuViewModels.reset_entry(tfIdBarang, tfNamaBarang,tfHargaBarang, tfStokBarang)),
            relief="flat"
        )
        btbEdit.place(
            x=1095.0,
            y=288.0,
            width=106.0,
            height=54.0
        )

        self.canvas.create_rectangle(
            791.0,
            111.0,
            1268.0,
            288.0,
            fill="#282828",
            outline="")

        self.canvas.create_rectangle(
            799.0,
            117.0,
            1258.0,
            281.0,
            fill="#838383",
            outline="")

        tfNamaBarangImage = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            1082.0,
            179.0,
            image=tfNamaBarangImage
        )
        tfNamaBarang = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
        )
        tfNamaBarang.place(
            x=919.0,
            y=167.0,
            width=326.0,
            height=22.0
        )

        self.canvas.create_text(
            812.0,
            171.0,
            anchor="nw",
            text="Nama Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )

        tfStokBarangImage = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            1082.0,
            216.0,
            image=tfStokBarangImage
        )
        tfStokBarang = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
        )
        tfStokBarang.place(
            x=919.0,
            y=204.0,
            width=326.0,
            height=22.0
        )

        tfHargaBarangImage = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            1082.0,
            253.0,
            image=tfHargaBarangImage
        )
        tfHargaBarang = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
        )
        tfHargaBarang.place(
            x=919.0,
            y=241.0,
            width=326.0,
            height=22.0
        )
        
        binder_cmd = (self.window.register(lambda P: self.validate_price_input(P, tfHargaBarang)), '%P')
        tfHargaBarang.config(validatecommand=binder_cmd)

        totalBarangVar = StringVar()
        tfTotalBarangImage = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            1101.0,
            614.0,
            image=tfTotalBarangImage
        )
        tfTotalBarang = Entry(
            bd=0,
            textvariable=totalBarangVar,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
            state='readonly',
        )
        tfTotalBarang.place(
            x=972.0,
            y=602.0,
            width=258.0,
            height=22.0
        )

        totalStokVar = StringVar()
        tfTotalStokImage = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            1101.0,
            644.0,
            image=tfTotalStokImage
        )
        tfTotalStok = Entry(
            bd=0,
            textvariable=totalStokVar,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
            state='readonly'
        )
        tfTotalStok.place(
            x=972.0,
            y=632.0,
            width=258.0,
            height=22.0
        )

        lastUpdate = StringVar()
        tfLastUpdateImage = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            1101.0,
            674.0,
            image=tfLastUpdateImage
        )
        tfLastUpdate = Entry(
            bd=0,
            textvariable=lastUpdate,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
            state='readonly'
        )
        tfLastUpdate.place(
            x=972.0,
            y=662.0,
            width=258.0,
            height=22.0
        )

        self.canvas.create_text(
            872.0,
            208.0,
            anchor="nw",
            text="Stok:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )

        tfIdBarangImage = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            1082.0,
            142.0,
            image=tfIdBarangImage
        )
        tfIdBarang = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
        )
        tfIdBarang.place(
            x=919.0,
            y=130.0,
            width=326.0,
            height=22.0
        )

        self.canvas.create_text(
            838.0,
            134.0,
            anchor="nw",
            text="ID Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )

        self.canvas.create_text(
            863.0,
            245.0,
            anchor="nw",
            text="Harga:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )
        
        
        self.tree.bind("<Double-1>", lambda event: self.mainMenuViewModels.tree_on_double_click(self.tree, tfIdBarang, tfNamaBarang, tfHargaBarang, tfStokBarang))
        
        self.mainMenuViewModels.init_update_status_entry([totalBarangVar, totalStokVar, lastUpdate])
        
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def numeric_checker(self, char):
        # Fungsi ini memeriksa apakah karakter yang dimasukkan adalah digit
        return char.isdigit()

    def validate_price_input(self, char, entry):
        # Fungsi ini akan dipanggil setiap kali pengguna mencoba memasukkan karakter
        if not self.numeric_checker(char):
            return False
        # Jika karakter valid, update entry
        return True