from tkinter import END, filedialog
from UI_helper.create_elements import CreateElement


class pathField:
    def __init__(self, master) -> None:
        self.creator =  CreateElement()
        self.path_field = self.creator.create_label_frame(master, "Set Path", p_x=10, p_y=10)
        self.path_width = 60

    def create_entries(self):
        self.set_python_path = self.creator.create_entrie(self.path_field, self.path_width, "C:/Python37/python.exe")
        self.set_robot_path = self.creator.create_entrie(self.path_field, self.path_width, "C:/ws/Robotframework")
        
    def create_buttons(self):
        menu_text = "..."
        self.change_python_bttn = self.creator.create_button(self.path_field, menu_text)
        self.change_robot_bttn = self.creator.create_button(self.path_field, menu_text)

    def allign_entries(self):
        self.set_python_path.grid(row=0, column=0)
        self.set_robot_path.grid(row=1, column=0)

    def allign_buttons(self):
        self.change_python_bttn.grid(row=0, column=1, padx=10, pady=10)
        self.change_robot_bttn.grid(row=1, column=1)

    def set_button_commands(self):
        self.change_python_bttn.config(command=lambda : self.filepicker("p"))
        self.change_robot_bttn.config(command=lambda : self.filepicker("r"))

    def filepicker(self, filepicker_type):
        if filepicker_type == "p":
            v = filedialog.askopenfilename(initialdir="/", title="Select file", 
                                           filetypes=(("Python file", ".py"), ("all_files", "*.*")))
            self.set_python_path.delete(0, END)
            self.set_python_path.insert(0, v)
        else:
            v = filedialog.askdirectory()
            self.set_robot_path.delete(0, END)
            self.set_robot_path.insert(0, v)

    def get_path_field(self):
        self.create_entries()
        self.create_buttons()
        self.allign_entries()
        self.allign_buttons()
        self.set_button_commands()
        return self.path_field