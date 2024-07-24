# Method Overloading:


class MultiUtils:
    def add(self, a, b, c=0):
        return a + b + c

math = MultiUtils()
p1 = math.add(4, 2)
p2 = math.add(4, 2, 4)
print(p1)
print(p2)