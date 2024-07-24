class Father:
    def father_money(self):
        return 5
    def home(self):
        return "This is from father"

class Mother:
    def mother_money(self):
        return 2
    def home(self):
        return "This is from mother"

class Son(Father, Mother):
    def home(self):
        return "This is from son"

son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home())