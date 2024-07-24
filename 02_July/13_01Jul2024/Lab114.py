#multilevel inheritance

class GrandFather:
    key_gold = "55kg"
    def grand_father_method(self):
        print("Grand Father")

class Father(GrandFather):
    def father_method(self):
        print("Father")

class Son(Father):
    mac_app = True
    def son_method(self):
        print("Son")

# Create an instance of the Son class
son = Son()
son.son_method()  # Output: Son
print(son.key_gold)  # Output: 55kg
print(son.mac_app)  # Output: True

print("----------------------------")
parent = Father()
parent.father_method()
parent.grand_father_method()
print(parent.key_gold)
print("----------------------------")
grand_parent = GrandFather()
grand_parent.grand_father_method()
print(grand_parent.key_gold)
