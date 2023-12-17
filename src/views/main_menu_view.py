
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class MainMenu:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"D:\CODE\Python\School\DASPRO GUI\FIGMA\page 2\build\assets\frame1")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        window = Tk()

        window.title("Aplikasi Pendataan")
        window.geometry("1280x720")
        window.configure(bg = "#282727")


        canvas = Canvas(
            window,
            bg = "#282727",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            22.0,
            117.0,
            782.0,
            703.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            22.0,
            25.0,
            anchor="nw",
            text="Data Barang",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 40 * -1)
        )

        canvas.create_rectangle(
            22.0,
            76.0,
            265.0,
            83.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            791.0,
            575.0,
            1268.0,
            709.0,
            fill="#282828",
            outline="")

        canvas.create_rectangle(
            799.0,
            584.0,
            1258.0,
            703.0,
            fill="#838383",
            outline="")

        canvas.create_text(
            858.0,
            604.0,
            anchor="nw",
            text="Total Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 16 * -1)
        )

        canvas.create_text(
            818.0,
            634.0,
            anchor="nw",
            text="Total Stok Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 16 * -1)
        )

        canvas.create_text(
            818.0,
            664.0,
            anchor="nw",
            text="Terakhir Diupdate:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 16 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=976.0,
            y=288.0,
            width=106.0,
            height=54.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=855.0,
            y=288.0,
            width=108.0,
            height=57.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=1095.0,
            y=288.0,
            width=106.0,
            height=54.0
        )

        canvas.create_rectangle(
            791.0,
            111.0,
            1268.0,
            288.0,
            fill="#282828",
            outline="")

        canvas.create_rectangle(
            799.0,
            117.0,
            1258.0,
            281.0,
            fill="#838383",
            outline="")

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            1082.0,
            179.0,
            image=entry_image_1
        )
        entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=919.0,
            y=167.0,
            width=326.0,
            height=22.0
        )

        canvas.create_text(
            812.0,
            171.0,
            anchor="nw",
            text="Nama Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            1082.0,
            216.0,
            image=entry_image_2
        )
        entry_2 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=919.0,
            y=204.0,
            width=326.0,
            height=22.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            1082.0,
            253.0,
            image=entry_image_3
        )
        entry_3 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=919.0,
            y=241.0,
            width=326.0,
            height=22.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            1101.0,
            614.0,
            image=entry_image_4
        )
        entry_4 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=972.0,
            y=602.0,
            width=258.0,
            height=22.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            1101.0,
            644.0,
            image=entry_image_5
        )
        entry_5 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_5.place(
            x=972.0,
            y=632.0,
            width=258.0,
            height=22.0
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(
            1101.0,
            674.0,
            image=entry_image_6
        )
        entry_6 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_6.place(
            x=972.0,
            y=662.0,
            width=258.0,
            height=22.0
        )

        canvas.create_text(
            872.0,
            208.0,
            anchor="nw",
            text="Stok:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )

        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = canvas.create_image(
            1082.0,
            142.0,
            image=entry_image_7
        )
        entry_7 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_7.place(
            x=919.0,
            y=130.0,
            width=326.0,
            height=22.0
        )

        canvas.create_text(
            838.0,
            134.0,
            anchor="nw",
            text="ID Barang:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )

        canvas.create_text(
            863.0,
            245.0,
            anchor="nw",
            text="Harga:",
            fill="#FFFFFF",
            font=("Rubik SemiBold", 14 * -1)
        )
        window.resizable(False, False)
        window.mainloop()
