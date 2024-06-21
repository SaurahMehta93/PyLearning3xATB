details = { "name": "Saurabh", "age": 31}

print(details.get("name"))
print(details.get("age"))
print(details.values())
print(details.keys())


my_dict = {"a": 1, "b": 2, "c": 3, "a": 95, "d": 95}
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for i in list(my_dict.values()):
    print(i)

for k, v in my_dict.items():
    print(k, v)