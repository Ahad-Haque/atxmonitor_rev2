# incoming.py

from tkinter import Canvas, Button, PhotoImage

class IncomingPage:
    def __init__(self, parent, relative_to_assets):
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

        self.rounded_corner_rect_img = PhotoImage(
            file=relative_to_assets("roundedCornerRectangle.png"))
        self.image_1 = self.canvas.create_image(
            397.0,
            184.0,
            image=self.rounded_corner_rect_img
        )

        self.outgoing_btn_img = PhotoImage(
            file=relative_to_assets("outgoingBtnImg.png"))
        self.outgoing_btn = Button(
            self.canvas,
            image=self.outgoing_btn_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("outgoingBtn clicked"),
            relief="flat"
        )
        self.outgoing_btn.place(
            x=442.0,
            y=322.0,
            width=89.0,
            height=24.705883026123047
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            795.0,
            44.0,
            fill="#3120FF",
            outline="")

        self.canvas.create_text(
            345.0,
            10.0,
            anchor="nw",
            text="INCOMING",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.label_img = PhotoImage(
            file=relative_to_assets("labelImg.png"))
        self.image_2 = self.canvas.create_image(
            99.0,
            184.0,
            image=self.label_img
        )

        self.equalsign_img = PhotoImage(
            file=relative_to_assets("equalsignImg.png"))
        self.image_3 = self.canvas.create_image(
            178.0,
            184.0,
            image=self.equalsign_img
        )

        self.create_text_items()

    def create_text_items(self):
        positions = [83, 114, 145, 176, 207, 238, 269]
        for pos in positions:
            self.canvas.create_text(
                192.0,
                pos,
                anchor="nw",
                text="999999",
                fill="#000000",
                font=("Inter Bold", 16 * -1)
            )

    def show(self):
        #self.canvas.place(x=0, y=0)
        self.canvas.tkraise()  # bring the canvas to the front

    def hide(self):
        self.canvas.place_forget()  # lower the canvas behind other elements

    def destroy(self):
        self.canvas.destroy()  # destroy the canvas and its elements
