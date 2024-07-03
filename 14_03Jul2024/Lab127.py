class my_custom_exception(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter amount to withdraw:"))

if withdraw > balance:
    raise my_custom_exception("Insufficient Balance")
else:
    balance = balance - withdraw
    print("Withdraw successful. Remaining balance:", balance)
