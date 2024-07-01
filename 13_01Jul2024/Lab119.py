class Father:
    def home(self):
        print("Father's home")

class Son(Father):
    def home(self):
        super().home()
        print("Son's home")


s1 = Son()
s1.home()