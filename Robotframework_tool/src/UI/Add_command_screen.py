from tkinter import E, RIGHT, W, Toplevel
from UI_helper.create_elements import CreateElement


class AddCommand:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.window = Toplevel(master)
        self.window.title("Add a Command")
        self.window.geometry("350x350")
        self.added_commands = {}

        self.saved_command_name = 1
        self.latest_added_command = ""

        self.entry_width = 20
        self.standard_padding = 10

    def create_frame(self):
        self.command_frame = self.creator.create_label_frame(self.window, "Add Command")
        self.added_commands_frame = self.creator.create_label_frame(self.window, "Saved Commands")
        self.command_frame.grid(row=0, column=0, padx=self.standard_padding)
        self.added_commands_frame.grid(row=1, column=0, padx=self.standard_padding, sticky=W)

    def create_label(self):
        self.command_name_lable = self.creator.create_lable(self.command_frame, "Command Name")
        self.command_value_lable = self.creator.create_lable(self.command_frame, "Command Value")
        self.saved_name_lable = self.creator.create_lable(self.added_commands_frame, "Name")
        self.saved_value_lable = self.creator.create_lable(self.added_commands_frame, "Value")

    def create_entry(self):
        self.command_name = self.creator.create_entrie(self.command_frame, self.entry_width)
        self.command_value = self.creator.create_entrie(self.command_frame, self.entry_width)

    def create_button(self):
        self.add_bttn = self.creator.create_button(self.command_frame, "Add")
        self.remove_bttn = self.creator.create_button(self.added_commands_frame, "Remove")
        self.add_bttn.config(command=lambda : self.add_command())
        self.remove_bttn.config(command=lambda : self.remove_command())

    def allign_entry(self):
        self.command_name.grid(row=1, column=0, padx=self.standard_padding, pady=self.standard_padding)
        self.command_value.grid(row=1, column=1, padx=self.standard_padding, pady=self.standard_padding)

    def allign_button(self):
        self.add_bttn.grid(row=2, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)
        self.remove_bttn.grid(row=1, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)

    def allign_label(self):
        self.command_name_lable.grid(row=0, column=0)
        self.command_value_lable.grid(row=0, column=1)
        self.saved_name_lable.grid(row=0, column=0)
        self.saved_value_lable.grid(row=0, column=1)

    def update_command_display(self, name, value):
        self.lable_add_name = self.creator.create_lable(self.added_commands_frame, name)
        self.lable_add_value = self.creator.create_lable(self.added_commands_frame, value)
        self.remove_bttn.grid(row=(self.saved_command_name+1))
        self.lable_add_name.grid(row=self.saved_command_name, column=0)
        self.lable_add_value.grid(row=self.saved_command_name, column=1)
        self.saved_command_name += 1
        
    def add_command(self):
        name = self.command_name.get()
        value = self.command_value.get()
        self.added_commands[name] = value
        self.update_command_display(name, value)
        self.latest_added_command = name

# # Doesn't work yet:
# Implementation should be with a list
# ... which contains the dictonaries for the added values

    def remove_command(self):
        del self.added_commands[self.latest_added_command]
        self.lable_add_name.grid_remove()
        self.lable_add_value.grid_remove()
        self.saved_command_name -= 1

    def get_commands(self):
        return self.added_commands

    def create_window(self):
        self.create_frame()
        self.create_entry()
        self.create_button()
        self.create_label()
        self.allign_entry()
        self.allign_button()
        self.allign_label()
