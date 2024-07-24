# unpacking tuple
a,b,c = (29, 52, 125)

t = (29, 52, 125)
new_t = t + (4,)
print(new_t)

my_list = list(t)
print(my_list)
my_list.append(12)
new_t1 = tuple(my_list)
print(new_t1)


eni_api_url = tuple(["test.com/get", "abc.com/post", "def.com/delete"])
print(eni_api_url)
