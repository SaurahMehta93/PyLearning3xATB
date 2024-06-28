class VMLogin:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "admin@test.com" and self.password == "1234":
            print("Login Successful")
        else:
            print("Login Failed")

a1 = VMLogin("admin@test.com", "1234")
a1.login_confirm()

a2 = VMLogin("admin@test.com", "123456")
a2.login_confirm()

a3 = VMLogin("test@test.com", "1234")
a3.login_confirm()