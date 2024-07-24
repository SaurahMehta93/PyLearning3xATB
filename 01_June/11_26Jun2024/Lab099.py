class Calc:

    def __init__(self):
        print("Calc init")

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


cal_exe = Calc()
print(cal_exe.add(1, 2))
print(cal_exe.sub(4, 2))
print(cal_exe.mul(2, 2))
print(cal_exe.div(4, 2))