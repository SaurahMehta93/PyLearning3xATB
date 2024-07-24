def outer_function():
    v1 = 30
    v2 = 10
    def inner_function1():
        print(v1)
    def inner_function2():
        print(v2)

    inner_function1()

    inner_function2()


outer_function()