from tkinter import E, RIGHT, Toplevel
from UI_helper.create_elements import CreateElement


class AddCommand:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.window = Toplevel(master)
        self.window.title("Add a Command")
        self.window.geometry("350x150")
        self.added_commands = {}

        self.entry_width = 20
        self.standard_padding = 10

    def create_frame(self):
        self.command_frame = self.creator.create_label_frame(self.window, "Add Command")
        self.command_frame.grid(row=0, column=0)

    def create_label(self):
        self.command_name_lable = self.creator.create_lable(self.command_frame, "Command Name")
        self.command_value_lable = self.creator.create_lable(self.command_frame, "Command Value")

    def create_entry(self):
        self.command_name = self.creator.create_entrie(self.command_frame, self.entry_width)
        self.command_value = self.creator.create_entrie(self.command_frame, self.entry_width)

    def create_button(self):
        self.add_bttn = self.creator.create_button(self.command_frame, "Add")

    def allign_entry(self):
        self.command_name.grid(row=1, column=0, padx=self.standard_padding, pady=self.standard_padding)
        self.command_value.grid(row=1, column=1, padx=self.standard_padding, pady=self.standard_padding)

    def allign_button(self):
        self.add_bttn.grid(row=2, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)

    def allign_label(self):
        self.command_name_lable.grid(row=0, column=0)
        self.command_value_lable.grid(row=0, column=1)

    def update_command_display(self, name, value):
        pass

    def add_command(self):
        name = self.command_name.get()
        value = self.command_value.get()
        self.added_commands[name] = value

    def create_window(self):
        self.create_frame()
        self.create_entry()
        self.create_button()
        self.create_label()
        self.allign_entry()
        self.allign_button()
        self.allign_label()
