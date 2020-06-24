# Uses python3
from math import log2, ceil
import random


def merge(arr, left, mid, right):
    n_left = mid - left
    n_right = right - mid + 1
    n = right - left + 1
    n_inversions = 0
    L = arr[left:mid]
    R = arr[mid:right + 1]
    result = []
    l = 0
    r = 0
    while l < n_left and r < n_right:
        if L[l] <= R[r]:
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1
            n_inversions += n_left - l
    while l < n_left:
        result.append(L[l])
        l += 1
    while r < n_right:
        result.append(R[r])
        r += 1
    for i in range(n):
        arr[left + i] = result[i]
    return n_inversions


def merge_sort(arr, verbose=False):
    n_inversions = 0
    max_pow = int(ceil(log2(len(arr))))
    sizes = [2 ** i for i in range(max_pow)]
    for size in sizes:
        for left in range(0, len(arr) - 1, 2 * size):
            mid = min(left + size, len(arr)-1)
            right = min(left + 2 * size - 1, len(arr) - 1)
            if verbose:
                print(
                    "size =", size,
                    "left =", left,
                    "mid =", mid,
                    "right =", right
                )
                print("pre: arr=", arr)
            delta = merge(arr, left, mid, right)
            n_inversions += delta
            if verbose:
                print("post: n=", n_inversions, " arr=", arr)
    return n_inversions


def count_inversions_naive(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                result += 1
    return result


def stress_test(n_trials=1000):
    for _ in range(n_trials):
        try:
            length = random.randint(3, 10)
            arr_src = [random.randint(0, 10) for _ in range(length)]

            arr_expected = sorted(arr_src)
            n_expected = count_inversions_naive(arr_src)

            arr = arr_src.copy()
            n = merge_sort(arr)
        except:
            print(arr_src)
            raise

        msg = "{}=={}".format(arr_expected, arr)
        assert arr_expected == arr, msg
        msg = "{}=={} {}".format(n_expected, n, arr_src)
        assert n_expected == n, msg


if __name__ == '__main__':
    # stress_test()
    # arr = [10, 4, 5, 3, 7, 3, 7, 5, 10, 6]
    n = input()
    arr = [int(x) for x in input().split()]
    if arr:
        result = merge_sort(arr)
        print(result)
    else:
        print(0)
