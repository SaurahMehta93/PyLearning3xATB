import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Start time:", start_time)
        print("End time:", end_time)
        print("Time taken:", end_time - start_time)
    return wrapper()

@time_decorator
def log_function():
    time.sleep(5)
    print("print the log of time taken")

#log_function()


@time_decorator
def report_fun():
    time.sleep(2)
    print("print the report of time taken")

#report_fun()