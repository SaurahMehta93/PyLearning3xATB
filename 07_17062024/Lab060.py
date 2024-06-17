# Leap year

y1 = int(input("Enter the year: "))

if (y1 % 4 == 0 and y1 % 100 != 0) or (y1 % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")