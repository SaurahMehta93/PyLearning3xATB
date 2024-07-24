class GF:
    def home(self):
        print("Home 1")

class F(GF):
    def home(self):
        print("Home 2")

class S(F):
    def home(self):
        print("Home 3")


s = S()
s.home()