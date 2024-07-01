# Hierarchical inheritance

class Father:
    def BHK1(self):
        print("This is father's BHK1")

class Saurabh(Father):
    def BHK2(self):
        print("This is Saurabh's BHK2")

class Demo(Father):
    def BHK3(self):
        print("This is Demo's BHK3")

class Chotu(Father):
    def NoHouse(self):
        print("Chotu's has no house")

saurabh = Saurabh()
saurabh.BHK1()
saurabh.BHK2()

demo = Demo()
demo.BHK1()
demo.BHK3()

chotu = Chotu()
chotu.BHK1()
chotu.NoHouse()

