class Person:
    # Class variable
    name = "amit"
    age = None

    def walk(self):
        a = 10 # local variable
        print("I am method")
        print("Hi", self.age)


amit = Person()
amit.walk()