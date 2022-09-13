from tkinter import Frame
from UI_helper.create_elements import CreateElement


class bottomButtons:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.bottom_button = Frame(master)
        self.stndrd_bttn_width = 10

    def create_buttons(self):
        self.cancel = self.creator.create_button(self.bottom_button, "Cancel", width_value=self.stndrd_bttn_width)
        self.run = self.creator.create_button(self.bottom_button, "Run", width_value=self.stndrd_bttn_width)
        self.advanced = self.creator.create_button(self.bottom_button, "Advanced", width_value=self.stndrd_bttn_width)

    def allign_buttons(self):
        self.cancel.grid(row=0, column=2, padx=10)
        self.run.grid(row=0, column=1, padx=10)
        self.advanced.grid(row=0, column=0, padx=10)

    def get_bottom_button(self):
        self.create_buttons()
        self.allign_buttons()
        return self.bottom_button
