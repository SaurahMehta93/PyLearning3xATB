def decorator1(func):
    def wrapper():
        print("This is badri")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("This is awesome")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello")

say_hello()
