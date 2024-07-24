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

email=input("Enter the email \n")
password=input("Enter the password \n")
a1 = VWOLoginPage(email, password)
a1.login_confirm()
