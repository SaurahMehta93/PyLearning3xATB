try:
    n1 = int(input('Enter a number1: '))
    n2 = int(input('Enter a number2: '))
    result = n1/n2
except ValueError as e:
    print(e)
except ZeroDivisionError as e1:
    print(e1)
else:
    print(f"result is {result}")
finally:
    print("Thanks for using this")


