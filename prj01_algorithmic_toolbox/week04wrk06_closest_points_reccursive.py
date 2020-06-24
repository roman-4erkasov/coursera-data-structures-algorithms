# Uses python3
import random
from math import sqrt


def get_distance(point1, point2):
    if point1 is None or point2 is None:
        return None
    else:
        return sqrt(
            (point1[0] - point2[0]) ** 2
            +
            (point1[1] - point2[1]) ** 2
        )


def get_xdistance(point1, point2):
    if point1 is None or point2 is None:
        return None
    else:
        return abs(point1[0] - point2[0])


def get_ydistance(point1, point2):
    if point1 is None or point2 is None:
        return None
    else:
        return abs(point1[1] - point2[1])


def get_min_distance_naive(points, return_points=None):
    closest_points = None
    min_distance = None
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            point2 = points[j]
            point1 = points[i]
            distance = get_distance(point1, point2)
            if min_distance is None or distance < min_distance:
                min_distance = distance
                closest_points = (point1, point2)
    if return_points:
        return min_distance, closest_points
    else:
        return min_distance  # , closest_points


def get_inter_min(points, min_init, verbose=None):
    n_points = len(points)
    dist_min = min_init
    if verbose:
        print(
            "[get_inter_min][start] dist_min={} points={}".format(
                dist_min,
                points
            )
        )
    for i in range(n_points):
        for j in range(i + 1, n_points):
            dist_y = get_ydistance(points[i], points[j])
            dist = get_distance(points[i], points[j])
            if verbose:
                print(
                    "[get_inter_min][loop] points={} dist={} dist_min".format(
                        (points[i], points[j]), dist, dist_min
                    )
                )

            if dist_y > dist_min:
                break
            if dist_min is None or dist < dist_min:
                dist_min = dist

    if verbose:
        print(
            "[get_inter_min][finish] min={}".format(
                dist_min
            )
        )
    return dist_min


def get_reccursion(points_x, points_y, verbose=None):
    n_points = len(points_x)
    if verbose:
        print("get_reccursion: start: points_x={} points_y={}".format(points_x,points_y))
    if n_points <= 3:
        if verbose:
            print("get_reccursion: n={}<=4".format(n_points))
        d_min = get_min_distance_naive(points_x)
        if verbose:
            print("get_reccursion: d_min={}".format(d_min))
        return d_min
    else:
        idx_mid = n_points // 2
        point_mid = points_x[idx_mid]
        left_x = points_x[:idx_mid+1]
        right_x = points_x[idx_mid+1:]
        left_y = []
        right_y = []
        for p in points_y:
            if p[0] <= point_mid[0]:
                left_y.append(p)
            else:
                right_y.append(p)
        if verbose:
            print(
                "get_reccursion: left_x={} right_x={}".format(
                    left_x, right_x
                )
            )
            print(
                "get_reccursion: left_y={} right_y={}".format(
                    left_y, right_y
                )
            )
        left_min = get_reccursion(left_x, left_y,verbose)
        right_min = get_reccursion(right_x, right_y,verbose)
        if left_min is not None and right_min is not None:
            d_min = min(left_min,right_min)
        elif left_min is not None:
            d_min = left_min
        elif right_min is not None:
            d_min = right_min
        else:
            d_min = None
        points_inter = [p for p in points_y if get_xdistance(p, point_mid) <= d_min]
        inter_min = get_inter_min(points_inter, d_min, verbose=verbose)
        if verbose:
            print("get_reccursion: d_min={} inter_min={}".format(d_min,inter_min))
        if inter_min is None:
            return d_min
        else:
            return min(d_min, inter_min)


def get_min_distance(points,verbose=None):
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])
    return get_reccursion(points_x, points_y,verbose)


def stress_test(n_trials=1000):
    """
    :param n_trials:
    :return:
    """
    for _ in range(n_trials):
        length = random.randint(5, 20)
        points = [
            (random.randint(0, 10), random.randint(0, 10))
            for _ in range(length)
        ]
        expected = get_min_distance_naive(points)
        actual = get_min_distance(points,False)
        msg = "{}=={} {}".format(expected, actual, points)
        assert expected == actual, msg


def test1():
    """
    assert expected == actual, msg
    AssertionError: 1.0==1.4142135623730951 [(6, 9), (7, 4), (9, 9), (1, 5), (10, 4), (9, 0), (8, 8), (7, 2), (9, 6), (4, 8), (4, 9)]
    """
    points = [(6, 9), (7, 4), (9, 9), (1, 5), (10, 4), (9, 0), (8, 8), (7, 2), (9, 6), (4, 8), (4, 9)]

    print(get_min_distance(points, verbose=1), get_min_distance_naive(points))

def test2():
    """
        assert expected == actual, msg
    AssertionError: 1.4142135623730951==2.23606797749979 [(1, 5), (9, 6), (9, 10), (3, 1), (8, 7), (6, 6)]
    :return:
    """
    points = [(1, 5), (9, 6), (9, 10), (3, 1), (8, 7), (6, 6)]
    print(get_min_distance(points, verbose=1), get_min_distance_naive(points))

def test3():
    """
        assert expected == actual, msg
AssertionError: 1.4142135623730951==2.23606797749979 [(1, 5), (9, 6), (9, 10), (3, 1), (8, 7), (6, 6)]
    :return:
    """
    points = [(1, 5), (9, 6), (9, 10), (3, 1), (8, 7), (6, 6)]
    print(get_min_distance(points, verbose=1), get_min_distance_naive(points,return_points=1))


def run_interactive():
    n = int(input())
    points = []
    for _ in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
    print(get_min_distance(points))


if __name__ == '__main__':
    # stress_test()
    # test3()
    run_interactive()
