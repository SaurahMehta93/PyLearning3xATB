class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected"
        self.__private_var = "private"

    def __private_metdho(self):
        print("Private method called")

    def print_name(self):
        if self.__private_var == "private":
            self.__private_metdho()

        print("i am public method")

c1 = Car()
##c1.public_var = "public"
c1.print_name()
