t = ("Testing Academy", "SDET", "Learn Dhyan")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6, 3}
my_list = set.union(set1, set2)
print(my_list)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9, 10}
my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)

my_set = set2.difference(set1)
print(my_set)
