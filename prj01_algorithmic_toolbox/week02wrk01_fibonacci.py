# Uses python3
from math import sqrt

# def calc_fib(n):
#     if n <= 1:
#         return n
#     return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib(n):
    return int((((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n)/sqrt(5))


n = int(input())
print(calc_fib(n))
