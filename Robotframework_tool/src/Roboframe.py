from tkinter import *
from Create_UI import MainScreen



def start_program():
    root = Tk()
    MainScreen(root)
    root.mainloop() 


class Construct:

    def __init__(self, screen):
        self.root = screen
        self.get_tag_options()

    def construct_command(self):
        return

    def get_tag_options(self):
        v1, v2 = self.root.tag_state()
        if v1 != "Empty":
            print(v1)
        elif v2 != "Empty":
            print(v1, v2)

start_program()