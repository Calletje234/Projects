from tkinter import *
from tkinter import filedialog
from tkcalendar import DateEntry


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Roboframe")
        self.master.geometry("650x650")
        self.create_frames()
        self.create_entries()
        self.create_buttons()
        self.create_checkboxes()

    def create_frames(self):
        self.set_paths = LabelFrame(self.master, text="Set Path", padx=10, pady=10)
        self.options = LabelFrame(self.master, text="Options", padx=10, pady=10)
        self.buttons = Frame(self.master)
        self.set_paths.grid(padx=10, pady=10, row=0, column=0)
        self.options.grid(padx=10, pady=10, row=1, column=0)
        self.buttons.grid(padx=10, pady=10, row=3)

    def create_entries(self):
        python_path = StringVar(self.set_paths, "C:/Python37/python.exe")
        robot_path = StringVar(self.set_paths, "C:/ws/cmge.automation/RobotFrameworkCMGE")
        self.t_inc = StringVar(self.options)
        self.t_exc = StringVar(self.options)
        self.tst_include = StringVar(self.options)
        self.tst_exclude = StringVar(self.options)
        self.suite_inc = StringVar(self.options)
        self.suite_exc = StringVar(self.options)

        self.set_path_python = Entry(self.set_paths, width=60, textvariable=python_path)
        self.set_path_robot = Entry(self.set_paths, width=60, textvariable=robot_path)
        self.tags_inc_ent = Entry(self.options, width=80, state=DISABLED, textvariable=self.t_inc)
        self.tags_exc_ent = Entry(self.options, width=80, state=DISABLED, textvariable=self.t_exc)
        self.tst_inc_ent = Entry(self.options, width=80, state=DISABLED, textvariable=self.tst_include)
        self.tst_exc_ent = Entry(self.options, width=80, state=DISABLED, textvariable=self.tst_exclude)
        self.st_inc_ent = Entry(self.options, width=80, state=DISABLED, textvariable=self.suite_inc)
        self.st_exc_ent = Entry(self.options, width=80, state=DISABLED, textvariable=self.suite_exc)

        self.set_path_python.grid(row=0, column=0)
        self.set_path_robot.grid(row=1, column=0)
        self.tags_inc_ent.grid(row=1, column=2)
        self.tags_exc_ent.grid(row=2, column=2)
        self.tst_inc_ent.grid(row=4, column=2)
        self.tst_exc_ent.grid(row=5, column=2)
        self.st_inc_ent.grid(row=7, column=2)
        self.st_exc_ent.grid(row=8, column=2)

    def create_buttons(self):
        self.change_python_bttn = Button(self.set_paths, text="...", height=1, width=2,
                                         command=lambda: self.filepicker("p"))
        self.change_robot_bttn = Button(self.set_paths, text="...", height=1, width=2,
                                        command=lambda: self.filepicker("r"))
        self.cancel = Button(self.buttons, text="Cancel", width=10, command=lambda : self.master.destroy())
        self.run = Button(self.buttons, text="Run", width=10, command=lambda : Construct(self.master))
        self.advanced = Button(self.buttons, text="Advanced", width=10,
                               command=lambda : Advanced_options(self.master))

        self.change_python_bttn.grid(row=0, column=1, padx=10, pady=10)
        self.change_robot_bttn.grid(row=1, column=1)
        self.cancel.grid(row=0, column=2, padx=10)
        self.run.grid(row=0, column=1, padx=10)
        self.advanced.grid(row=0, column=0, padx=10)

    def create_checkboxes(self):
        self.tag_checkvar = IntVar()
        self.tag_inc_checkvar = IntVar()
        self.tag_exc_checkvar = IntVar()
        self.tst_checkvar = IntVar()
        self.tst_inc_checkvar = IntVar()
        self.tst_exc_checkvar = IntVar()
        self.st_checkvar = IntVar()
        self.st_inc_checkvar = IntVar()
        self.st_exc_checkvar = IntVar()
        
        self.tag = Checkbutton(self.options, text="Tags", variable=self.tag_checkvar,
                                   command=lambda : self.check_checkbox_tags("c_t"))
        self.tag_inc = Checkbutton(self.options, text="Include",variable=self.tag_inc_checkvar, state=DISABLED,
                                   command=lambda : self.check_checkbox_tags("c_i_t"))
        self.tag_exc = Checkbutton(self.options, text="Exclude",variable=self.tag_exc_checkvar, state=DISABLED,
                                   command=lambda : self.check_checkbox_tags("c_e_t"))
        self.tst = Checkbutton(self.options, text="Test",variable=self.tst_checkvar,
                                   command=lambda : self.check_checkbox_tst("c_tst"))
        self.tst_inc = Checkbutton(self.options, text="Include",variable=self.tst_inc_checkvar, state=DISABLED,
                                   command=lambda : self.check_checkbox_tst("c_tst_i"))
        self.tst_exc = Checkbutton(self.options, text="Exclude",variable=self.tst_exc_checkvar, state=DISABLED,
                                   command=lambda : self.check_checkbox_tst("c_tst_e"))
        self.st = Checkbutton(self.options, text="Suite",variable=self.st_checkvar,
                                  command=lambda : self.check_checkbox_suite("c_s"))
        self.st_inc = Checkbutton(self.options, text="Include",variable=self.st_inc_checkvar, state=DISABLED,
                                  command=lambda : self.check_checkbox_suite("c_s_i"))
        self.st_exc = Checkbutton(self.options, text="Exclude",variable=self.st_exc_checkvar, state=DISABLED,
                                  command=lambda : self.check_checkbox_suite("c_s_e"))

        self.tag.grid(row=0, column=0)
        self.tag_inc.grid(row=1, column=1)
        self.tag_exc.grid(row=2, column=1)
        self.tst.grid(row=3, column=0)
        self.tst_inc.grid(row=4, column=1)
        self.tst_exc.grid(row=5, column=1)
        self.st.grid(row=6, column=0)
        self.st_inc.grid(row=7, column=1)
        self.st_exc.grid(row=8, column=1)

    def check_checkbox_tst(self, type):
        if type == "c_tst" and self.tst_checkvar.get() == 1:
            self.tst_inc.config(state=NORMAL)
            self.tst_exc.config(state=NORMAL)
        elif type == "c_tst" and self.tst_checkvar.get() == 0:
            self.tst_inc.config(state=DISABLED)
            self.tst_exc.config(state=DISABLED)
        elif type == "c_tst_i" and self.tst_inc_checkvar.get() == 1:
            self.tst_inc_ent.config(state=NORMAL)
        elif type == "c_tst_i" and self.tst_inc_checkvar.get() == 0:
            self.tst_inc_ent.config(state=DISABLED)
        elif type == "c_tst_e" and self.tst_exc_checkvar.get() == 1:
            self.tst_exc_ent.config(state=NORMAL)
        elif type == "c_tst_e" and self.tst_exc_checkvar.get() == 0:
            self.tst_exc_ent.config(state=DISABLED)

    def check_checkbox_suite(self, type):
        if type == "c_s" and self.st_checkvar.get() == 1:
            self.st_inc.config(state=NORMAL)
            self.st_exc.config(state=NORMAL)
        elif type == "c_s" and self.st_checkvar.get() == 0:
            self.st_inc.config(state=DISABLED)
            self.st_exc.config(state=DISABLED)
        elif type == "c_s_i" and self.st_inc_checkvar.get() == 1:
            self.st_inc_ent.config(state=NORMAL)
        elif type == "c_s_i" and self.st_inc_checkvar.get() == 0:
            self.st_inc_ent.config(state=DISABLED)
        elif type == "c_s_e" and self.st_exc_checkvar.get() == 1:
            self.st_exc_ent.config(state=NORMAL)
        elif type == "c_s_e" and self.st_exc_checkvar.get() == 0:
            self.st_exc_ent.config(state=DISABLED)

    def check_checkbox_tags(self, type):
        if type == "c_t" and self.tag_checkvar.get() == 1:
            self.tag_inc.config(state=NORMAL)
            self.tag_exc.config(state=NORMAL)
        elif type == "c_t" and self.tag_checkvar.get() == 0:
            self.tag_inc.config(state=DISABLED)
            self.tag_exc.config(state=DISABLED)
        elif type == "c_i_t" and self.tag_inc_checkvar.get() == 1:
            self.tags_inc_ent.config(state=NORMAL)
        elif type == "c_i_t" and self.tag_inc_checkvar.get() == 0:
            self.tags_inc_ent.config(state=DISABLED)
        elif type == "c_e_t" and self.tag_exc_checkvar.get() == 1:
            self.tags_exc_ent.config(state=NORMAL)
        elif type == "c_e_t" and self.tag_exc_checkvar.get() == 0:
            self.tags_exc_ent.config(state=DISABLED)
     
    def filepicker(self, file):
        if file == "p":
            v = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("Python file", ".py"), ("all_files", "*.*")))
            self.set_path_python.delete(0, END)
            self.set_path_python.insert(0, v)
        else:
            v = filedialog.askdirectory()
            self.set_path_robot.delete(0, END)
            self.set_path_robot.insert(0, v)

    def tag_state(self):
        if self.tag_inc['state'] == NORMAL:
            v1 = self.t_inc.get()
            v2 = "Empty"
        elif self.tag_exc['state'] == NORMAL:
            v1 = self.t_exc.get()
            v2 = "Empty"
        elif self.tag_exc['state'] == NORMAL and self.tag_inc['state'] == NORMAL:
            v1 = self.t_inc.get()
            v2 = self.t_exc.get()
        else:
            v1 = "Empty"
            v2 = "Empty"

        return v1, v2

class Advanced_options():
    def __init__(self, master):
        self.master = master
        self.window = Toplevel(master)
        self.window.title("Advanced_options")
        self.window.geometry("650x650")
        self.create_frame()
        self.create_buttons()
        self.create_date_picker()
        self.create_checkboxes()
        self.create_input_fields()

    def create_buttons(self):
        self.add_var = Button(self.bottum, text="Add", command=lambda : AddVar(self.master))
        self.add_var.grid(row=0, column=0, padx=10, pady=10)

    def create_checkboxes(self):
        self.date_checkvar = IntVar()
        self.own_cmd = IntVar()

        self.cmd_check = Checkbutton(self.middel, text="Add Own Commands", variable=self.own_cmd, 
                                      command=lambda : self.check_own_cmd())
        self.date_check = Checkbutton(self.top, text="Plan a run", variable=self.date_checkvar,
                                      command=lambda : self.check_tag())
        self.date_check.grid(row=0, column=0)
        self.cmd_check.grid(row=0, column=0)

    def create_frame(self):
        self.top = LabelFrame(self.window, text="Plan a Run")
        self.middel = LabelFrame(self.window, text="Add own Commands")
        self.date_picker = LabelFrame(self.top, text="Date Picker")
        self.bottum = LabelFrame(self.window, text="Variables")
        self.time = LabelFrame(self.top, text="Time Picker")
        self.cmd = LabelFrame(self.middel, text="Command")

        self.bottum.grid(row=2, column=0, padx=10, pady=10)
        self.cmd.grid(row=1, column=0, padx=10, pady=10)
        self.top.grid(row=0, column=0, padx=10)
        self.middel.grid(row=1, column=0, padx=10, pady=10)
        self.date_picker.grid(row=1, column=0, padx=10)
        self.time.grid(row=1, column=1, padx=10, pady=10)

    def create_input_fields(self):
        self.time_checkvar = IntVar()
        self.own_command_entry = Entry(self.cmd, state=DISABLED, width=80)
        self.time_picker = Entry(self.time, state=DISABLED)

        self.time_picker.grid(row=0, column=0, padx=5, pady=5)
        self.own_command_entry.grid(row=0, column=0, padx=5, pady=5)
    
    def check_add_var(self):
        if self.add_chechvar.get() == 1:
            self.add_own_vars_name.config(state=NORMAL)
            self.add_own_vars_key.config(state=NORMAL)
        else:
            self.add_own_vars_name.config(state=DISABLED)
            self.add_own_vars_key.config(state=DISABLED)

    def check_own_cmd(self):
        if self.own_cmd.get() == 1:
            self.own_command_entry.config(state=NORMAL)
        else:
            self.own_command_entry.config(state=DISABLED)

    def check_tag(self):
        if self.date_checkvar.get() == 1:
            self.cal.config(state=NORMAL)
            self.time_picker.config(state=NORMAL)
        elif self.date_checkvar.get() == 0:
            self.cal.config(state=DISABLED)
            self.time_picker.config(state=DISABLED)

    def create_date_picker(self):
        self.cal = DateEntry(self.date_picker, width=12, state=DISABLED)
        self.cal.grid(row=1, column=0, padx=5,pady=5)

class AddVar:
    def __init__(self, mainFrame):
        self.master = mainFrame
        self.var_window = Toplevel(mainFrame)
        self.var_window.geometry("350x150")
        self.var_window.title("Add Variable")
        self.add_frames()
        self.add_entry()
        self.add_buttons()

    def add_buttons(self):
        self.add = Button(self.bottum, text="Add")

        self.add.grid(row=0, column=0)

    def add_frames(self):
        self.top = LabelFrame(self.var_window, text="Variable Values")
        self.bottum = Frame(self.var_window)
        self.add_name = LabelFrame(self.top, text="Variable Name")
        self.add_val = LabelFrame(self.top, text="Variable Value")
        
        self.bottum.grid(row=1, column=0)
        self.top.grid(row=0, column=0, padx=10)
        self.add_name.grid(row=0, column=0, padx=10, pady=10)
        self.add_val.grid(row=0, column=1, padx=10, pady=10)

    def add_entry(self):
        self.add_var_name_value = StringVar(self.add_name)
        self.add_var_key_value = StringVar(self.add_val)
        self.add_var_name = Entry(self.add_name, textvariable=self.add_var_name_value)
        self.add_var_value = Entry(self.add_val, textvariable=self.add_var_key_value)

        self.add_var_name.grid(row=0, column=0, padx=5, pady=5)
        self.add_var_value.grid(row=0, column=0, padx=5, pady=5)
        


