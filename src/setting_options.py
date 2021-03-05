
class setting_options():
    command = ""

    def tag_options(self):
        start = True
        while start:
            print("Do you want to include or exclude tags?")
            c = input("In / Ex: ")
            if c.lower() == 'in':
                self.command += f"--include {self.get_tags()}"
            elif c.lower() == 'ex':
                self.command += f"--exclude {self.get_tags()}"
            else:
                print("Please use 'In' or 'Ex' to specify")

    def get_tags(self):
        print("Please enter the tags you want to include or exclude")
        print("NOTE: If you want to provide multiple tags use ',' to seperate them")
        tags = input("TAGS: ")
        tags.replace(',','AND').strip().replace(' ', "")
        ''.join(tags.split())

    def tst_options(self):
        self.command += f'--test "{self.specific_tst()}"'

    def specific_tst(self):
        print("Which specific test do you want to run?")
        print("NOTE: If you want to include multiple tests use ',' to seperate them")
        tst = input("TESTS: ")
        s1 = "["
        s2 = "]"
        tst.replace(',','|').strip().replace(' ', "")
        ''.join(tst.split())
        tst = s1+tst+s2

    def suite_options(self):
        self.command += f'--suite {self.specific_suite()}'

    def specific_suite(self):
        print("Which specific suite do you want to run?")
        suite = input("SUITE: ")
        



        

