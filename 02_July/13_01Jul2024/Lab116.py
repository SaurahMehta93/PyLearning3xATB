class ClassA:
    def methodA(self):
        print("Method A")

class ClassB(ClassA):
    def methodB(self):
        print("Method B")


class ClassC(ClassA):
    def methodC(self):
        print("Method C")

class ClassD(ClassB, ClassC):
    def methodD(self):
        print("Method D")


d = ClassD()
d.methodA()
d.methodB()
d.methodC()
d.methodD()

