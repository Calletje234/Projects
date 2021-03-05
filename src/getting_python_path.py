import sys

class getting_python_path():
    command = ""
    python_VERSION = ""

    def __init__(self, python_version):
        self.python_VERSION = sys.version
        self.python_VERSION.replace(".", '')
        python_map_version = self.python_VERSION[0:1]
        self.python_VERSION = python_map_version

    def python_folder(self, path="DEFAULT"):
        if path == "DEFAULT":
            path = f"C:\Python{self.python_VERSION}\python.exe "
        else:
            print("Please enter the path to you're Python File!")
            path = self.path_python()
        self.command += path
        return self.command

    def path_python(self):
        checking_path = True
        while checking_path:
            path = input("path: ")
            print("Is the following path Correct?")
            print(path)
            correct = input("Y \ N")
            if correct.upper() == "Y":
                checking_path = False
                return path
            else:
                print("Please Try Again")
