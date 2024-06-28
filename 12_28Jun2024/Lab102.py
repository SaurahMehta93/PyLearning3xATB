
class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model
    def start_engline(self):
        print("starting a car with the name " + self.name)
        print("starting a car with the make " + self.make)
        print("starting a car with the model " + self.model)

car1 = Car("lambogini", "urus", "2018")
car1.start_engline()

car2 = Car("ferrari", "enzo", "2002")
car2.start_engline()
