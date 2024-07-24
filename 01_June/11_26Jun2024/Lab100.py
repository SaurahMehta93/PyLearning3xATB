class Student:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

st = Student()
st.display()