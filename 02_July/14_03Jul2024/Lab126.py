class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number: "))
        except Exception as e:
            print("enter only integer")
        else:
            print(a)
        finally:
            print("thank you")

obj = XYZ()
obj.f1()
