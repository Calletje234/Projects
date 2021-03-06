from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

from RobotFramework_tool.Robotframework_tool.GUI import Advanced_screen


class main_screen():
    root = Tk()
    root.title("RoboFrame")
    root.geometry("650x650")

    #initialize all frame variables
    set_path = ""
    set_options = ""
    bottum_btn = ""

    #initialize all checkboxes variables
    tag = ""
    tag_inc = ""
    tag_exc = ""
    tst = ""
    tst_inc = ""
    tst_exc = ""
    st = ""
    st_inc = ""
    st_exc = ""

    #initialize all buttons variables
    change_python_bttn = ""
    change_rf_bttn = ""
    adv_opt_bttn = ""
    cancel = ""
    run = ""

    #initialize all entries variables
    folder_python = ""
    folder_rf = ""
    tags_inc_ent = ""
    tags_exc_ent = ""
    tst_inc_ent = ""
    tst_exc_ent = ""
    st_inc_ent = ""
    st_exc_ent = ""

    def construct_mainscreen(self):
        self.setup_frames()
        self.set_checkboxes()
        self.create_buttons()
        self.create_entries()
        self.create_output_field()
        self.construct_maingrid()
        self.format_screen()

    def construct_maingrid(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=3)
        
    def format_screen(self):
        self.tag.grid(row=0,column=0)
        self.tst.grid(row=3,column=0)
        self.st.grid(row=6,column=0)
        self.tag_inc.grid(row=1,column=1)
        self.tag_exc.grid(row=2,column=1)
        self.tst_inc.grid(row=4,column=1)
        self.tst_exc.grid(row=5,column=1)
        self.st_inc.grid(row=7,column=1)
        self.st_exc.grid(row=8,column=1)
        
        self.change_python_bttn.grid(row=0,column=3,padx=10,pady=10)
        self.change_rf_bttn.grid(row=1,column=3)
        self.adv_opt_bttn.grid(row=12,column=1,padx=10)
        self.run.grid(row=12,column=2,padx=10)
        self.cancel.grid(row=12,column=3, padx=10)

        #Set Entry Collums
        self.folder_python.grid(row=0,column=0)
        self.folder_rf.grid(row=1,column=0)
        self.tags_inc_ent.grid(row=1,column=2)
        self.tags_exc_ent.grid(row=2,column=2)
        self.tst_inc_ent.grid(row=4,column=2)
        self.tst_exc_ent.grid(row=5,column=2)
        self.st_inc_ent.grid(row=7,column=2)
        self.st_exc_ent.grid(row=8,column=2)

    def set_checkboxes(self):
        self.tag = Checkbutton(self.options, text = "Tags")
        self.tag_inc = Checkbutton(self.options, text="Include")
        self.tag_exc = Checkbutton(self.options, text="Exclude")
        self.tst = Checkbutton(self.options, text="Test")
        self.tst_inc = Checkbutton(self.options, text="Include")
        self.tst_exc = Checkbutton(self.options, text="Exclude")
        self.st = Checkbutton(self.options, text="Suite")
        self.st_inc = Checkbutton(self.options, text="Include")
        self.st_exc = Checkbutton(self.options, text="Exclude")

    def create_buttons(self):
        self.change_python_bttn = Button(self.set_paths, text="...", height=1,width=2, state=NORMAL, command=lambda : self.filepicker("pyt"))
        self.change_rf_bttn = Button(self.set_paths, text="...", height=1, width=2, state=NORMAL, command=lambda : self.filepicker("rf"))
        #command : lambda function doens't work yet
        self.adv_opt_bttn = Button(self.bottum_btn, text="Advanced", command=lambda : Advanced_screen.construct_advance_options_screen(), width=10)
        #-----------------------------------------------------------------------------------------------------------------------------------------#
        self.cancel = Button(self.bottum_btn, text="Cancel", width=10)
        self.run = Button(self.bottum_btn, text="Run", width=10)

    def filepicker(self, pyt):
        if pyt == "pyt":
           file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Python file",".py"),("all files","*.*")))
           self.folder_python.delete(0, END)
           self.folder_python.insert(0, file)
        else:
            folder = filedialog.askdirectory()
            self.folder_rf.delete(0, END)
            self.folder_rf.insert(0, folder)
            
    def create_entries(self):
        pythonv = StringVar(self.set_paths, "C:/Python37/pyhton.exe")
        rfv= StringVar(self.set_paths, "C:/ws/cmge.automation/RobotFrameworkCMGE")
        self.folder_python = Entry(self.set_paths, width=60, textvariable=pythonv)
        self.folder_rf = Entry(self.set_paths, width=60, textvariable=rfv)
        self.tags_inc_ent = Entry(self.options, width=80)
        self.tags_exc_ent = Entry(self.options, width=80)
        self.tst_inc_ent = Entry(self.options, width=80)
        self.tst_exc_ent = Entry(self.options, width=80)
        self.st_inc_ent = Entry(self.options, width=80)
        self.st_exc_ent = Entry(self.options, width=80)

    def create_output_field(self):
        return

    def setup_frames(self):
        bottum_btn = Frame(self.root)
        bottum_btn.grid(row=3, column=0)

        set_paths = LabelFrame(self.root, text="Set Path", padx=10, pady=10)
        options = LabelFrame(self.root, text="Options", padx=10, pady=10)
        set_paths.grid(row=0, column=0)
        options.grid(row=1, column=0)
        self.set_paths = set_paths
        self.options = options
        
    def mainloop(self):
        self.root.mainloop()

t = main_screen()
t.construct_mainscreen()
t.mainloop()
