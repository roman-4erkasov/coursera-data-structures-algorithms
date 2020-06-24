# Uses python3
import sys
from queue import Queue

"""
5 1 2 3 4 5
5 5 4 3 0 1

5 1 5 8 12 13
5 8 1 23 1 11
"""


def binary_search(a, x, verbose=False):
    left, right = 0, len(a) - 1
    # write your code here
    while right-left>1:
        mid = int((left + right) / 2.)
        if verbose:
            print("\nleft=",left,"mid=",mid,"right=",right,"x=",x)
        if x in {a[left], a[mid], a[right]}:
            break
        if a[mid] > x:
            right = mid
        elif a[mid] < x:
            left = mid
    if a[left] == x:
        return left
    elif a[mid] == x:
        return mid
    elif a[right] == x:
        return right
    else:
        return -1

    # que = Queue()
    # que.put((left, right))
    # while not que.empty():
    #     left, right = que.get()
    #     if verbose: print("1)", left, right, "(", x, ")")
    #     if right - left > 1:
    #         mid = int((left + right) / 2.)
    #         if verbose:
    #             print("2)", mid, "(", x, ")")
    #         if a[mid] > x:
    #             if verbose:
    #                 print("que.put((", left, ", ", mid, "))")
    #             que.put((left, mid))
    #         elif a[mid] <= x:
    #             if verbose:
    #                 print("que.put((", mid, ", ", right, "))")
    #             que.put((mid, right))
    #     elif a[left] == x:
    #         return left
    #     elif a[right] == x:
    #         return right
    # return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    row1 = [int(x) for x in input().split()]
    row2 = [int(x) for x in input().split()]
    # input_ = sys.stdin.read()
    # data1 = list(map(int, input().split()))
    n = row1[0]
    m = row2[0]
    a = row1[1:]
    for x in row2[1:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end=' ')
