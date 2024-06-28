# Webautomation - Selenium

# Page - you are going automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password=="Password123":
            print("Login Successful")
        else:
            print("Login Failed")
    #This is end of the class


a1 = VWOLoginPage("test@test.com", "Password123")
a1.login_confirm()

a2 =  VWOLoginPage("demo@test.com", "Passwor2d123")
a2.login_confirm()