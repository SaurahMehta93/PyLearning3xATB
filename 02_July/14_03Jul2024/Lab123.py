
try:
    a = int(input("Enter the number1: "))
    b = int(input("Enter the number2: "))
    c = a/b # ZeroDivisionError
    print(c)
except Exception as e:
    print("Exception caught: ", e)
