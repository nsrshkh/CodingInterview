from GeneralConcepts import timer

# def Fibonacci(n):
#
#     if n < 0:
#         print("Incorrect input")
#
#     elif n == 0:
#         return 0
#
#     elif n == 1 or n == 2:
#         return 1
#
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
# print(Fibonacci(9))



# def fibonacci(n):
#     l = [0, 1]
#     for i in range(2, n):
#         l = l + [l[-1] + l[-2]]
#     return l
#
# print(fibonacci(20))
#
# print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])

@timer
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print the first 10 Fibonacci numbers
fib_gen = fibonacci_sequence()
for _ in range(10):
    print(next(fib_gen))