from UI_helper.create_elements import CreateElement
from tkinter import *


class createEntryField:
    def __init__(self, master) -> None:
        self.creator = CreateElement()
        self.options = self.creator.create_label_frame(master, "Options", p_x=10, p_y=10)        
        self.path_width = 60
        self.inc_exc_width = 80
        self.python_standard_text = "C:/Python37/python.exe"
        self.robot_standard_text = "C:/ws/robotframework"


    def create_entries(self):
        self.tags_inc = self.creator.create_entrie(self.options, self.inc_exc_width, state_value=DISABLED)
        self.tags_exc = self.creator.create_entrie(self.options, self.inc_exc_width, state_value=DISABLED)
        self.test_inc = self.creator.create_entrie(self.options, self.inc_exc_width, state_value=DISABLED)
        self.test_exc = self.creator.create_entrie(self.options, self.inc_exc_width, state_value=DISABLED)

    def create_checkbox(self):
        include_text = "Include"
        exclude_text = "Exclude"
        self.check_tag_checker = IntVar()
        self.check_tag_inc_checker = IntVar()
        self.check_tag_exc_checker = IntVar()
        self.check_test_checker = IntVar()
        self.check_test_inc_checker = IntVar()
        self.check_test_exc_checker = IntVar()

        self.check_tag = self.creator.create_checkbox(self.options, "Tags", self.check_tag_checker)
        self.check_tag_inc = self.creator.create_checkbox(self.options, include_text, self.check_tag_inc_checker, state_value=DISABLED)
        self.check_tag_exc = self.creator.create_checkbox(self.options, exclude_text, self.check_tag_exc_checker, state_value=DISABLED)
        self.check_test = self.creator.create_checkbox(self.options, "Test", self.check_test_checker)
        self.check_test_inc = self.creator.create_checkbox(self.options, include_text, self.check_test_inc_checker, state_value=DISABLED)
        self.check_test_exc = self.creator.create_checkbox(self.options, exclude_text, self.check_test_exc_checker, state_value=DISABLED)

    def set_checkbox_commands(self):
        self.check_tag.config(command=lambda : self.check_checkbox_tag("tag_check"))
        self.check_tag_inc.config(command=lambda : self.check_checkbox_tag("tag_check_inc"))
        self.check_tag_exc.config(command=lambda : self.check_checkbox_tag("tag_check_exc"))
        self.check_test.config(command=lambda : self.check_checkbox_test("test_check"))
        self.check_test_inc.config(command=lambda : self.check_checkbox_test("test_check_inc"))
        self.check_test_exc.config(command=lambda : self.check_checkbox_test("test_check_exc"))

    def allign_entries(self):
        self.tags_inc.grid(row=1, column=2)
        self.tags_exc.grid(row=2, column=2)
        self.test_inc.grid(row=4, column=2)
        self.test_exc.grid(row=5, column=2)
    
    def allign_checkboxes(self):
        self.check_tag.grid(row=0, column=0)
        self.check_tag_inc.grid(row=1, column=1)
        self.check_tag_exc.grid(row=2, column=1)
        self.check_test.grid(row=3, column=0)
        self.check_test_inc.grid(row=4, column=1)
        self.check_test_exc.grid(row=5, column=1)

    def check_checkbox_test(self, check_name):
        if check_name == "test_check" and self.check_test_checker.get() == 1:
            self.check_test_inc.config(state=NORMAL)
            self.check_test_exc.config(state=NORMAL)
        elif check_name == "test_check" and self.check_test_checker.get() == 0:
            self.check_test_inc.config(state=DISABLED)
            self.check_test_exc.config(state=DISABLED)
            self.check_test_inc_checker.set(0)
            self.check_test_exc_checker.set(0)
        elif check_name == "test_check_inc" and self.check_test_inc_checker.get() == 1:
            self.test_inc.config(state=NORMAL)
        elif check_name == "test_check_inc" and self.check_test_inc_checker.get() == 0:
            self.test_inc.config(state=DISABLED)
        elif check_name == "test_check_exc" and self.check_test_exc_checker.get() == 1:
            self.test_exc.config(state=NORMAL)
        elif check_name == "test_check_exc" and self.check_test_exc_checker.get() == 0:
            self.test_exc.config(state=DISABLED)
    
    def check_checkbox_tag(self, check_name):
        if check_name == "tag_check" and self.check_tag_checker.get() == 1:
            self.check_tag_inc.config(state=NORMAL)
            self.check_tag_exc.config(state=NORMAL)
        elif check_name == "tag_check" and self.check_tag_checker.get() == 0:
            self.check_tag_inc.config(state=DISABLED)
            self.check_tag_exc.config(state=DISABLED)
            self.check_tag_inc_checker.set(0)
            self.check_tag_exc_checker.set(0)
        elif check_name == "tag_check_inc" and self.check_tag_inc_checker.get() == 1:
            self.tags_inc.config(state=NORMAL)
        elif check_name == "tag_check_inc" and self.check_tag_inc_checker.get() == 0:
            self.tags_inc.config(state=DISABLED)
        elif check_name == "tag_check_exc" and self.check_tag_exc_checker.get() == 1:
            self.tags_exc.config(state=NORMAL)
        elif check_name == "tag_check_exc" and self.check_tag_exc_checker.get() == 0:
            self.tags_exc.config(state=DISABLED)

    def get_options_frame(self):
        self.create_entries()
        self.create_checkbox()
        self.allign_checkboxes()
        self.allign_entries()
        self.set_checkbox_commands()
        return self.options

    