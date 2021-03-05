import sys

class getting_robotframework_path():
    command = ""

    def rf_path(self, path="DEFAULT"):
        if path == "DEFAULT":
            path = ""
        else:
            path = self.rf_change_path()
        self.command += path
        return self.command

    def rf_change_path(self):
        checking_path = True
        with checking_path:
            path = input("path: ")
            print("Is the following path correct?")
            print(path)
            correct = input("Y / N: ")
            if correct.upper() == "Y":
                checking_path = False
                return path
            else:
                print("Please Try Again")