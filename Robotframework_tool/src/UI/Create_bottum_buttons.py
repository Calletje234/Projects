from doctest import master
from tkinter import Frame
from UI_helper.create_elements import CreateElement
from UI.Advanced_screen import advancedScreen


class bottumButtons:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.bottum_button = Frame(master)
        self.master = master
        self.stndrd_bttn_width = 10

    def create_buttons(self):
        self.cancel = self.creator.create_button(self.bottum_button, "Cancel", width_value=self.stndrd_bttn_width)
        self.run = self.creator.create_button(self.bottum_button, "Run", width_value=self.stndrd_bttn_width)
        self.advanced = self.creator.create_button(self.bottum_button, "Advanced", width_value=self.stndrd_bttn_width)

    def allign_buttons(self):
        self.cancel.grid(row=0, column=2, padx=10)
        self.run.grid(row=0, column=1, padx=10)
        self.advanced.grid(row=0, column=0, padx=10)

    def add_button_commands(self):
        self.cancel.config(command=lambda : self.master.destroy())
        self.advanced.config(command=lambda : advancedScreen(self.master).create_window())

    def get_bottum_button(self):
        self.create_buttons()
        self.allign_buttons()
        self.add_button_commands()
        return self.bottum_button
