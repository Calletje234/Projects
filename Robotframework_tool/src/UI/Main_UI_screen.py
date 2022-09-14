from tkinter import *
from UI.Create_entry_field import createEntryField
from UI.Create_path_field import pathField
from UI_helper.create_elements import CreateElement
from UI.Create_bottum_buttons import bottumButtons
from UI.Advanced_screen import advancedScreen

class mainScreen:
    def __init__(self, master) -> None:
        self.creator = CreateElement()

        self.master = master
        self.master.title("Roboframe")
        self.master.geometry("650x500")

        self.path_frame = pathField(self.master)
        self.options_frame = createEntryField(self.master)
        self.bottum_frame = bottumButtons(self.master)

        self.create_window()

    def create_window(self):
        path = self.path_frame.get_path_field()
        options = self.options_frame.get_options_frame()
        bottum = self.bottum_frame.get_bottum_button()
        path.grid(padx=10, pady=10, row=0, column=0)
        options.grid(padx=10, pady=10, row=1, column=0)
        bottum.grid(padx=10, pady=10, row=3)
