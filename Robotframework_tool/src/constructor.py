from Robotframework_tool.src import Create_UI


class construct():
    def __init__(self):
        self.get_tag_options()
        self.construct_command()

    def construct_command(self):
        return

    def get_tag_options(self):
        v1, v2 = Create_UI.main_screen.tag_state()
        if v1 != "Empty":
            print(v1)
        elif v2 != "Empty":
            print(v1, v2)


