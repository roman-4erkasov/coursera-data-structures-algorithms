# Uses python3
import random
from queue import Queue


def partition2(arr, left, right):
    # рандомизируем опорную точку
    rnd_idx = random.randint(left, right)
    arr[right], arr[rnd_idx] = arr[rnd_idx], arr[right]

    j = left - 1
    pivot = arr[right]

    for i in range(left, right):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[right] = arr[right], arr[j + 1]
    return j + 1


def quick(arr, verbose=False):
    buff = Queue()
    buff.put((0, len(arr) - 1))
    while not buff.empty():
        left, right = buff.get()  # block=False)
        if verbose:
            print("left=", left, "right=", right)
        if left < right:
            p = partition2(arr, left, right)
            if verbose:
                print("p=", p)
            buff.put((left, p - 1))  # ,block=False)
            buff.put((p + 1, right))  # ,block=False)
    return arr


def partition3(arr, left, right, verbose=False):
    # рандомизируем опорную точку
    rnd_idx = random.randint(left, right)
    pivot = arr[rnd_idx]
    # right bound of section with elements that less than pivot
    right_less = left - 1
    # left bound of section with elements that more than pivot
    left_more = right + 1
    if verbose:
        print("pivot=", pivot)
    i = left
    while i < left_more:
        if verbose:
            print("pre: arr[", i, "]=", arr[i], "(pivot=", pivot, "|", "arr2 =", arr, ")")
        if arr[i] < pivot:
            right_less += 1
            arr[i], arr[right_less] = arr[right_less], arr[i]
            i += 1
        elif arr[i] > pivot:
            left_more -= 1
            arr[i], arr[left_more] = arr[left_more], arr[i]
        else:
            i += 1
        if verbose:
            print("post: arr[", i, "]=", arr[i], "(pivot=", pivot, "|", "arr2 =", arr, ")")
    if verbose:
        print("arr2 =", arr)
    return right_less, left_more


def quick3(arr, verbose=False):
    buff = Queue()
    buff.put((0, len(arr) - 1))
    while not buff.empty():
        left, right = buff.get()  # block=False)
        if verbose:
            print("left=", left, "right=", right)
        if left < right:
            right_less, left_more = partition3(arr, left, right)
            if verbose:
                print("right_less=", right_less, "left_more=", left_more)
            if right_less >= 0:
                buff.put((left, right_less))  # ,block=False)
            if left_more < right:
                buff.put((left_more, right))  # ,block=False)
    return arr


if __name__ == '__main__':
    # print(quick3([random.randint(1, 9) for _ in range(20)]))
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = quick3(arr)
    print(" ".join([str(x) for x in result]))
