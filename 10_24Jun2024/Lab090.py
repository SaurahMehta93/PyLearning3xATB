



numbers = [1, 2, 3, 4, 5]

def doubler(numbers):
    return numbers * 2

def even_given(numbers):
    return numbers % 2 == 0

d = filter(doubler, numbers)
e = filter(even_given, numbers)

print(list(d))
print(list(e))