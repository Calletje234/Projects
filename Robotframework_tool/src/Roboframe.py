from tkinter import *
from Robotframework_tool.src import Create_UI


def start_program():
    root= Tk()
    Create_UI.main_screen(root)
    root.mainloop()

start_program()
