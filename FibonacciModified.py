import sys


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


sys.set_int_max_str_digits(0)  # to handle very large numbers


def fibonacciModified(t1, t2, n):
    i = 2
    res = 0
    while i < n:
        res = t1 + pow(t2, 2)
        t1 = t2
        t2 = res
        i += 1
    return res


t1 = 0
t2 = 1
n = 25

print(fibonacciModified(t1, t2, n))
