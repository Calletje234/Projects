from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

from tkcalendar import Calendar, DateEntry
from datetime import date

class main_screen():
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
        self.set_path_python = Entry(self.set_paths, width=60, textvariable=python_path)
        self.set_path_robot = Entry(self.set_paths, width=60, textvariable=robot_path)
        self.tags_inc_ent = Entry(self.options, width=80, state=DISABLED)
        self.tags_exc_ent = Entry(self.options, width=80, state=DISABLED)
        self.tst_inc_ent = Entry(self.options, width=80, state=DISABLED)
        self.tst_exc_ent = Entry(self.options, width=80, state=DISABLED)
        self.st_inc_ent = Entry(self.options, width=80, state=DISABLED)
        self.st_exc_ent = Entry(self.options, width=80, state=DISABLED)

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
        self.cancel = Button(self.buttons, text="Cancel", width=10)
        self.run = Button(self.buttons, text="Run", width=10)
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
                                   command=lambda : self.check_tag("c_t"))
        self.tag_inc = Checkbutton(self.options, text="Include",variable=self.tag_inc_checkvar, state=DISABLED,
                                   command=lambda : self.check_tag("c_i_t"))
        self.tag_exc = Checkbutton(self.options, text="Exclude",variable=self.tag_exc_checkvar, state=DISABLED,
                                   command=lambda : self.check_tag("c_e_t"))
        self.tst = Checkbutton(self.options, text="Test",variable=self.tst_checkvar,
                                   command=lambda : self.check_tag("c_tst"))
        self.tst_inc = Checkbutton(self.options, text="Include",variable=self.tst_inc_checkvar, state=DISABLED,
                                   command=lambda : self.check_tag("c_tst_i"))
        self.tst_exc = Checkbutton(self.options, text="Exclude",variable=self.tst_exc_checkvar, state=DISABLED,
                                   command=lambda : self.check_tag("c_tst_e"))
        self.st = Checkbutton(self.options, text="Suite",variable=self.st_checkvar,
                                  command=lambda : self.check_tag("c_s"))
        self.st_inc = Checkbutton(self.options, text="Include",variable=self.st_inc_checkvar, state=DISABLED,
                                  command=lambda : self.check_tag("c_s_i"))
        self.st_exc = Checkbutton(self.options, text="Exclude",variable=self.st_exc_checkvar, state=DISABLED,
                                  command=lambda : self.check_tag("c_s_e"))

        self.tag.grid(row=0, column=0)
        self.tag_inc.grid(row=1, column=1)
        self.tag_exc.grid(row=2, column=1)
        self.tst.grid(row=3, column=0)
        self.tst_inc.grid(row=4, column=1)
        self.tst_exc.grid(row=5, column=1)
        self.st.grid(row=6, column=0)
        self.st_inc.grid(row=7, column=1)
        self.st_exc.grid(row=8, column=1)

    def check_tag(self, type):
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
        elif type == "c_tst" and self.tst_checkvar.get() == 1:
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
        elif type == "c_s" and self.st_checkvar.get() == 1:
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

class Advanced_options():
    def __init__(self, master):
        self.window = Toplevel(master)
        self.window.title("Advanced_options")
        self.window.geometry("650x650")
        self.create_frame()
        self.create_date_picker()


    def create_frame(self):
        self.top = LabelFrame(text="Date Picker")
        self.bottum = LabelFrame(text="")

        self.top.grid(row=0, column=0, padx=10)
        self.bottum.grid(row=1, column=0)

    def create_date_picker(self):










root = Tk()
app = main_screen(root)
root.mainloop()