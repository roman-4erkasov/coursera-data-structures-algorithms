# python 3

def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def get_parent(index):
    return (index-1) // 2


def get_left_child(index):
    return 2 * index+1


def get_right_child(index):
    return 2 * index + 2


def sift_up(array, index):
    swaps = []
    # trg = index
    while index > 0 and array[get_parent(index)] > array[index]:
        array[index], array[get_parent(index)] = array[get_parent(index)], array[index]
        swaps.append((get_parent(index),index))
        index = get_parent(index)
    return swaps


def insert(arr, val):
    arr.append(val)
    sift_up(arr, len(arr) - 1)
    # return res


# def sift_down(arr, index):
#     target = index
#     left_child = 2 * index + 1
#     right_child = 2 * index + 2
#     n = len(arr)
#     if left_child < n and arr[left_child] < arr[index]:
#         arr[index], arr[left_child] = arr[left_child], arr[index]
#         target = left_child
#     elif right_child < n and arr[right_child] < arr[index]:
#         arr[index], arr[right_child] = arr[right_child], arr[index]
#         target = right_child
#     return index, target


def sift_down(arr, index):
    n = len(arr)
    index_changed = True
    swaps = []
    while index_changed:
        index_changed = False
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        src = index
        if left_child < n and arr[left_child] < arr[index]:
            index = left_child
            index_changed = True
        if right_child < n and arr[right_child] < arr[index]:
            index = right_child
            index_changed = True
        if index_changed:
            arr[index], arr[src] = arr[src], arr[index]
            swaps.append((src, index))
    return swaps


def build_heap(data):
    swaps = []
    heap = []
    # for v in enumerate(data):
    #     # print(heap)
    #     insert(heap, v)
    # for trg, (src, val) in enumerate(heap):
    #     swaps.append((src, trg))

    # for src in range(len(data) - 1, -1, -1):
    #     res = sift_up(data, src)
    #     # res = sift_down(data, src)
    #     swaps.extend(res)
    #     print(data)
    for src in range((len(data) - 1)//2, -1, -1):
        # res = sift_up(data, src)
        res = sift_down(data, src)
        swaps.extend(res)
        # print(data)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # print(data)


if __name__ == "__main__":
    main()
