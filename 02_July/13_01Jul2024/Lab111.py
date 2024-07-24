# Inheritance


class grand_father:
    key= "abc@123"
    def grand_father_method(self):
        print("This is grand father method")

class father(grand_father):
    def parent_method(self):
        print("This is father method")

gf = grand_father()
gf.grand_father_method()

parent = father()
parent.parent_method()
parent.grand_father_method()
print(parent.key)