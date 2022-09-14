from tkinter import E, W, Frame, Toplevel
from UI_helper.create_elements import CreateElement


class ErrorScreen:
    def __init__(self, master) -> None:
        self.window = Toplevel(master)
        self.creator = CreateElement()

        self.window.title("Wrong Action")
        self.window.geometry("250x100")

    def create_frame(self):
        self.error_frame = Frame(self.window)
        self.error_frame.grid(row=0)

    def create_buttons(self):
        self.ok_bttn = self.creator.create_button(self.error_frame, "OK")
        self.ok_bttn.config(command=lambda : self.window.destroy())

    def create_lable(self, error_msg):
        self.error_lable = self.creator.create_lable(self.error_frame, error_msg)

    def allign_items(self):
        self.error_lable.grid(padx=30, pady=5)
        self.ok_bttn.grid(row=1, padx=30, pady=5)

    def create_window(self, msg):
        self.create_frame()
        self.create_buttons()
        self.create_lable(msg)
        self.allign_items()