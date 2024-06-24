# Filter in Python

# The filter() function in python is built-in function
# Allows you to filter elements in the list, tuple, set

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter on the above -> even
#new_list_even = [2, 4, 6, 8, 10]

def is_even(num):
    return num % 2 == 0

new_numbers_event = filter(is_even, numbers)
print(list(new_numbers_event))