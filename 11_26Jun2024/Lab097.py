class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id
    def sleep(self):
        print("Who is sleeping " + self.name)


dog1 = Dog("Buddy", 1)
dog2 = Dog("Chow", 2)

dog1.sleep()
dog2.sleep()

print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')