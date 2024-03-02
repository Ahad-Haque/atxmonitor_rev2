# gui.py

from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from meter import MeterPage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\sayem\Desktop\ahad work\guioutput\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("795x420")
        self.root.configure(bg="#D7FFDD")

        self.canvas = Canvas(
            root,
            bg="#D7FFDD",
            height=420,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.current_content = None  # To keep track of the current content (image or frame)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("companyImg.png"))
        image_1 = self.canvas.create_image(
            397.0,
            132.0,
            image=self.image_image_1
        )

        self.meterBtnImg = PhotoImage(
            file=relative_to_assets("meterbtn.png"))
        meterBtn = Button(
            self.canvas,
            image=self.meterBtnImg,
            borderwidth=0,
            highlightthickness=0,
            command=self.load_meter_page,
            relief="flat"
        )
        meterBtn.place(
            x=73.0,
            y=373.494873046875,
            width=89.0,
            height=24.705883026123047
        )


        self.abountBtnImg = PhotoImage(
            file=relative_to_assets("aboutBtn.png"))
        aboutBtn = Button(
            image=self.abountBtnImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aboutBtn clicked"),
            relief="flat"
        )
        aboutBtn.place(
            x=213.0,
            y=373.494873046875,
            width=89.0,
            height=24.705883026123047
        )

        self.settingsBtnImg = PhotoImage(
            file=relative_to_assets("settingsBtn.png"))
        settingsBtn = Button(
            image=self.settingsBtnImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("settingsBtn clicked"),
            relief="flat"
        )
        settingsBtn.place(
            x=353.0,
            y=373.494873046875,
            width=89.0,
            height=24.705883026123047
        )

        self.historyBtnImg = PhotoImage(
            file=relative_to_assets("historyBtn.png"))
        historyBtn = Button(
            image=self.historyBtnImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("historyBtn clicked"),
            relief="flat"
        )
        historyBtn.place(
            x=493.0,
            y=373.494873046875,
            width=89.0,
            height=24.705883026123047
        )

        self.liveImgBtn = PhotoImage(
            file=relative_to_assets("liveBtn.png"))
        liveBtn = Button(
            image=self.liveImgBtn,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("liveBtn clicked"),
            relief="flat"
        )
        liveBtn.place(
            x=633.0,
            y=373.494873046875,
            width=89.0,
            height=24.705883026123047
        )
        

    def load_meter_page(self):
        # Remove the existing content
        if self.current_content:
            self.canvas.delete(self.current_content)

        # Create and show the MeterPage frame
        self.meter_page = MeterPage(self.canvas,relative_to_assets)
        self.meter_page.show()
        self.current_content = self.meter_page.canvas

if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()
