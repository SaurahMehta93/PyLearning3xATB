class Password:

    def __init__(self, pwd):
        self.__password = pwd
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print('Access denied')

    def set_password(self, pwd):
        if len(pwd) > 6:
            self.__password =pwd
            print("Password changed to", self.__password)
        else:
            print("Password must be at least 6 characters long")

p1 = Password("12521521")
p1.get_password(True)
p1.set_password("sag")
p1.set_password("saurabh")
