# Oops
# Object oriented porgramming

class Person:
    name = None
    age= None
    phone_number = None

    def talk(self):
        print("I am talk")

    def another(self):
        print("I am a method")

    def sleep(self, name):
        print("I am a method")
        print("Sleep", name)

    def sleep2(self, name):
        print("I am a method")
        return None

    def walk(self):
        print("I am a walk")

saurabh = Person()
saurabh.name = "Saurabh"
saurabh.age = 31
saurabh.phone_number= 750
saurabh.talk()
saurabh.another()
saurabh.sleep("Saurabh")
saurabh.sleep2("Saurabh")
saurabh.walk()

