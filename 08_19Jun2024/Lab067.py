# lambda arguments: expression

#def find_odd_event(n):
#    if n % 2 == 0:
#        return "Even"
#    else:
#        return "Odd"

#a = find_odd_event(5)
#b = find_odd_event(4)

#print(a)
#print(b)


check_odd_event = lambda n: "Odd" if n % 2 != 0 else "Even"
print(check_odd_event(5))
print(check_odd_event(4))