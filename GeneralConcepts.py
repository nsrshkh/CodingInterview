# with open('myfile.txt', 'w') as file:
#     file.write('DataCamp Black Friday Sale!!!')

# try:
#     num1 = int(input('Enter Numerator: '))
#     num2 = int(input('Enter Denominator: '))
#     division = num1/num2
#     print(f'Result is: {division}')
# except:
#     print('Invalid input!')
# else:
#     print('Division is successful.')


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()


# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# add(2, 3)

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        end = time.time_ns()
        print(f"{func.__name__} took {end-start:.9f} nanoseconds")
        return result
    return wrapper

# @timer
# def slow_function():
#     time.sleep(1)
#
# slow_function()