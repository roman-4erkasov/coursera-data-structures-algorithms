# Uses python3
import random
from functools import cmp_to_key


def cmp(l, r):
    less = l[0] < r[0] or \
        (l[0] == r[0] and l[1] == 'l' and r[1] in {'p', 'r'}) or \
        (l[0] == r[0] and l[1] in {'l', 'p'} and r[1] == 'r')
    more = l[0] > r[0] or \
        (l[0] == r[0] and l[1] in {'r', 'p'} and r[1] == 'l') or \
        (l[0] == r[0] and l[1] == 'r' and r[1] in {'p', 'l'})
    equal = l[0] == r[0] and l[1] == r[1]
    if less:
        return -1
    elif more:
        return 1
    elif equal:
        return 0
    else:
        msg = "l={} r={}".format(l, r)
        raise Exception(msg)


def lottery_hits(segments, points):
    result = [0] * len(points)

    axis = []
    for left, right in segments:
        axis.append((left, 'l', None))
        axis.append((right, 'r', None))
    for index, point in enumerate(points):
        axis.append((point, 'p', index))
    axis.sort(key=cmp_to_key(cmp))
    n_active_segments = 0
    for value, flag, index in axis:
        if flag == 'l':
            n_active_segments += 1
        elif flag == 'r':
            n_active_segments -= 1
        elif flag == 'p':
            result[index] += n_active_segments
    return result


def lottery_hits_naive(segments, points):
    result = [0] * len(points)
    for idx, point in enumerate(points):
        for left, right in segments:
            if left <= point <= right:
                result[idx] += 1
    return result


def test1():
    segments = [(0, 5), (7, 10)]
    points = [1, 6, 11]
    print("naive solution:", lottery_hits_naive(segments, points))
    print("target solution:", lottery_hits(segments, points))


def test2():
    segments = [(-10, 10)]
    points = [- 100, 100, 0]
    print("naive solution:", lottery_hits_naive(segments, points))
    print("target solution:", lottery_hits(segments, points))


def test3():
    segments = [(0, 5), (-3, 2), (7, 10)]
    points = [1, 6]
    print("naive solution:", lottery_hits_naive(segments, points))
    print("target solution:", lottery_hits(segments, points))


def stress_test(n_trials=1):
    for _ in range(n_trials):
        n_points = random.randint(3, 10)
        points = [random.randint(0, 10) for _ in range(n_points)]
        n_segments = random.randint(3, 10)
        # segments = [(random.randint(0, 10)) for _ in range(n_points)]
        segments = []
        for _ in range(n_segments):
            offset = random.randint(0, 10)
            length = random.randint(0, 10)
            left = offset
            right = offset + length
            segments.append((left, right))
        expected = lottery_hits_naive(segments, points)
        actual = lottery_hits(segments, points)
        msg = "{} == {}".format(expected, actual)
        assert expected == actual, msg


if __name__ == '__main__':
    # print(cmp(l=(7, 'p', 2), r=(7, 'r', None)))
    # stress_test(100)
    first_line = [int(x) for x in input().split()]
    s = int(first_line[0])
    p = int(first_line[1])
    segments = []
    for _ in range(s):
        segments.append([int(x) for x in input().split()])
    points = [int(x) for x in input().split()]
    print(" ".join([str(x) for x in lottery_hits(segments, points)]))
