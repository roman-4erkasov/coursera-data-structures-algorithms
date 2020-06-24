# Uses python3
import sys
from math import sqrt


# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10

def get_fibonacci_last_digit(n):
    prev = 0
    curr = 1
    for _ in range(1,n):
        prev, curr = curr%10, (prev%10+curr%10)%10
    return curr


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
