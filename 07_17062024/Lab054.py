# function
# block of code - which can executed or reused.


def say_hello(): #function with no parameter / arguments
    print("Hello")

#say_hello() #function call

def  say_hello(name): #function with parameter / arguments
    print(f"Hello {name}")

#say_hello("saurabh")
#say_hello("p")

def say_hello_arg_default(name="saurabh"):
    print(f"Hello {name}")

say_hello_arg_default()
say_hello_arg_default("saurabh")
say_hello_arg_default(name="mehta")


def sum_arg(a,b):
    print(a+b)

n1 = sum_arg(2, 3)
print(n1)
