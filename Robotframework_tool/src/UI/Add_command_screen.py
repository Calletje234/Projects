from operator import add
from time import sleep
from tkinter import E, RIGHT, W, Frame, Toplevel
from UI_helper.create_elements import CreateElement
from UI.Error_screen import ErrorScreen


class AddCommand:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.window = Toplevel(master)
        self.master = master
        self.window.title("Add a Command")
        self.window.geometry("350x350")
        self.added_commands = []

        self.saved_command_name = 1
        self.error_message = "There is nothing to remove"

        self.entry_width = 20
        self.standard_padding = 10

    def create_frame(self):
        self.command_frame = self.creator.create_label_frame(self.window, "Add Command")
        self.added_commands_frame = self.creator.create_label_frame(self.window, "Saved Commands")
        self.bottum_button = Frame(self.window)
        self.command_frame.grid(row=0, column=0, padx=self.standard_padding)
        self.added_commands_frame.grid(row=1, column=0, padx=self.standard_padding, sticky=W)
        self.bottum_button.grid(row=2)

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
        self.cancel_bttn = self.creator.create_button(self.bottum_button, "Cancel")
        self.add_bttn.config(command=lambda : self.add_command())
        self.remove_bttn.config(command=lambda : self.remove_command())
        self.cancel_bttn.config(command=lambda : self.window.destroy())

    def allign_entry(self):
        self.command_name.grid(row=1, column=0, padx=self.standard_padding, pady=self.standard_padding)
        self.command_value.grid(row=1, column=1, padx=self.standard_padding, pady=self.standard_padding)

    def allign_button(self):
        self.add_bttn.grid(row=2, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)
        self.remove_bttn.grid(row=1, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)
        self.cancel_bttn.grid(pady=self.standard_padding, sticky=W)

    def allign_label(self):
        self.command_name_lable.grid(row=0, column=0)
        self.command_value_lable.grid(row=0, column=1)
        self.saved_name_lable.grid(row=0, column=0)
        self.saved_value_lable.grid(row=0, column=1)
        
    def add_command(self):
        added_labels_dict = {}
        field_name = self.command_name.get()
        field_value = self.command_value.get()
        created_lable_name = self.creator.create_lable(self.added_commands_frame, field_name)
        created_lable_field = self.creator.create_lable(self.added_commands_frame, field_value)
        self.remove_bttn.grid(row=self.saved_command_name+1, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)
        created_lable_name.grid(row=self.saved_command_name, column=0)
        created_lable_field.grid(row=self.saved_command_name, column=1)
        added_labels_dict[created_lable_name] = created_lable_field
        self.added_commands.append(added_labels_dict)
        self.saved_command_name += 1

    def remove_command(self):
        if len(self.added_commands) == 0:
            ErrorScreen(self.master).create_window("There is no command to remove")
        else:
            remove_dict = self.added_commands[-1]
            for k in remove_dict:
                name = k
                value = remove_dict[k]
            name.grid_remove()
            value.grid_remove()
            self.added_commands.pop(-1)
            self.saved_command_name -= 1
            self.remove_bttn.grid(row=self.saved_command_name, column=1, padx=self.standard_padding, pady=self.standard_padding, sticky=E)

    def create_window(self):
        self.create_frame()
        self.create_entry()
        self.create_button()
        self.create_label()
        self.allign_entry()
        self.allign_button()
        self.allign_label()
