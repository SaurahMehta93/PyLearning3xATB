class bank_account:
    def __init__(self,  balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        print(f"Balance: {self.balance}")



account1 = bank_account(100)
account1.deposit(50)
account1.display_account_info()
account1.withdraw(75)
account1.display_account_info()
