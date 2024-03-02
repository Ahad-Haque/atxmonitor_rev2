# meter.py (converted)

from tkinter import Canvas, Button, PhotoImage
from incoming import IncomingPage  # Import the IncomingPage class
from pathlib import Path
from tkinter import Tk

class MeterPage:
    def __init__(self, parent, relative_to_assets):
        self.parent = parent
        self.relative_to_assets = relative_to_assets

        self.canvas = Canvas(
            parent,
            bg="#D7FFDD",
            height=350,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.button_image_1 = PhotoImage(file=relative_to_assets("incomingbtn.png"))
        self.button_image_2 = PhotoImage(file=relative_to_assets("outgoingbtn.png"))
        self.image_image_1 = PhotoImage(file=relative_to_assets("plcwithborder.png"))

        self.canvas.create_rectangle(
            0.0,
            0.0,
            795.0,
            44.0,
            fill="#3120FF",
            outline=""
        )

        self.canvas.create_text(
            362.0,
            10.0,
            anchor="nw",
            text="METER",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.image_1 = self.canvas.create_image(
            397.0,
            184.0,
            image=self.image_image_1
        )

        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.incomingfun(),
            relief="flat"
        )
        self.button_1.place(
            x=263.0,
            y=322.0,
            width=89.0,
            height=24.705883026123047
        )

        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=442.0,
            y=322.0,
            width=89.0,
            height=24.705883026123047
        )
    def incomingfun():
        print("Incoming button is pressed.")
    
    def outgoingfun():
        print("outgoing button is pressed.")

    def show(self):
        self.canvas.place(x=0, y=0)

    def hide(self):
        self.canvas.place_forget()  # lower the canvas behind other elements

    def destroy(self):
        self.canvas.destroy()  # destroy the canvas and its elements

    def show_incoming_page(self):
        # Hide the current MeterPage
        self.hide()
        
        # Create and show the IncomingPage frame
        incoming_page = IncomingPage(self.parent, self.relative_to_assets)
        incoming_page.show()
