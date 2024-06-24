#map


numbers = [1, 2, 3, 4, 5]

def double_me(num):
    return num * 2

new_list_double= map(double_me, numbers)
print(list(numbers))

#filters
# pick item m if true keep it false, remove it
# it can give less number of items as compare to actual
