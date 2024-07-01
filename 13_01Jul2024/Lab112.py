class Parent:
    gold = "2kb"
    def BHK2(self):
        print("2BHK flat")

class Child(Parent):
    def BHK3(self):
        print("3BHK flat")

child_obj = Child()
child_obj.BHK3()
child_obj.BHK2()
print(child_obj.gold)

parent_obj = Parent()
print(parent_obj.gold)
parent_obj.BHK2()
#print(parent_obj.BHK3())
