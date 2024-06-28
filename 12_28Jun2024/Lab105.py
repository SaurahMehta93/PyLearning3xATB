# Encapsulation

# bind the data variable with the methods

# Hide the data members(class vairable, instance variable) by using only the methods

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        self.password = "789"

c1 = Car()
c1.password = "456"
