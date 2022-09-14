from tkinter import *
from UI_helper.create_elements import CreateElement
from UI.Add_command_screen import AddCommand

class advancedScreen:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.master = master
        self.window = Toplevel(master)
        self.window.title("Advanced Options")
        self.window.geometry("650x650")

    def create_frames(self):
        self.top = self.creator.create_label_frame(self.window, "Add Own Commands")
        self.top.grid(row=0, column=0, padx=10)

    def create_buttons(self):
        self.add_command = self.creator.create_button(self.top, "Add")
        self.add_command.grid(row=0, column=0, padx=40, pady=10)

    def add_button_commands(self):
        self.add_command.config(command=lambda : AddCommand(self.master).create_window())

    def create_window(self): 
        self.create_frames()
        self.create_buttons()
        self.add_button_commands()