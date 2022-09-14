from tkinter import *
from UI.Main_UI_screen import mainScreen
from Create_UI import MainScreen


def start_program():
    root = Tk()
    mainScreen(root)
    root.mainloop()

start_program()