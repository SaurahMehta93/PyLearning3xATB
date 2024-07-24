class Parent:
    def __init__(self):
        print("Parent")


class Son(Parent):
    def __init__(self):
        super().__init__()

obj = Son()
