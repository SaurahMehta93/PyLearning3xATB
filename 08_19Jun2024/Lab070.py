my_list = [1, 2, 3, 4, 5]
# print(my_list * 2)  # Uncomment this line to print the list multiplied by 2

#temp_list = []
#for i in my_list:
#    temp_list.append(i * 2)

#print(temp_list)

#def double_items(num):
#    return num ** 2

double_items = lambda x: x ** 2
# map()
# 1. takes each item from the list
# 2. execute the function on it
# 3. return same number of elements (list)

double_list = list(map(double_items, my_list))
print(double_list)


print(list(map(lambda x: x ** 2, [1,2,3,4,5,6])))