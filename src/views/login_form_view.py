from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view_models import login_form_view_models as lvm
from views import main_menu_view as mainMenu

class LoginForm:
    def __init__(self):
        self.viewModel = lvm.LoginFormViewModel()
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.window = Tk()

        self.window.title("Aplikasi Pendataan")
        self.window.geometry("1280x720")
        self.window.configure(bg = "#282727")

        canvas = Canvas(
            self.window,
            bg = "#282727",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.viewModel.loginAction(entry_1.get(), entry_2.get(), self), 
            relief="flat"
        )
        button_1.place(
            x=832.0,
            y=487.0,
            width=299.0,
            height=74.0
        )

        canvas.create_rectangle(
            802.0,
            260.99999762505803,
            1161.6586480351566,
            309.5859166679129,
            fill="#282828",
            outline="")

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            981.5521167740126,
            285.4657066866652,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
        )
        entry_1.place(
            x=825.0,
            y=266.99998621304064,
            width=313.10423354802504,
            height=34.931440947249115
        )

        canvas.create_rectangle(
            801.0,
            386.00000636979325,
            1162.0601497248124,
            433.89004859052056,
            fill="#282828",
            outline="")

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            981.5521167740126,
            410.4657066866652,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Rubik", 14),
            show="*"
        )
        entry_2.place(
            x=825.0,
            y=391.99998621304064,
            width=313.10423354802504,
            height=34.931440947249115
        )

        canvas.create_rectangle(
            927.0,
            116.0,
            1036.0,
            122.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            919.0,
            63.0,
            anchor="nw",
            text="LOGIN",
            fill="#FFFFFF",
            font=("Rubik Bold", 40 * -1)
        )

        canvas.create_text(
            901.0,
            216.0,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Rubik Regular", 32 * -1)
        )

        canvas.create_text(
            905.0,
            341.0,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Rubik Regular", 32 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            330.8685108466707,
            350.0,
            image=image_image_1
        )
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def loadMainMenu(self):
        self.window.destroy()
        mainMenuUI = mainMenu.MainMenu()
