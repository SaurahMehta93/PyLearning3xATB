class Dog:
    name = None
    id = None

    def __init__(self):
        print("No argument")
    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id
    def sleep(self):
        print("Who is sleeping")


dog1 = Dog()
dog2 = Dog("Chow", 2)

print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')