# Uses python3
import random
from math import log2, ceil, sqrt

"""
This code is not completed :-(
"""


def get_min_distance_naive(points):
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
    return min_distance, closest_points


def test_get_min_distance_naive():
    points = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (2, 4)
    ]
    print(get_min_distance_naive(points))


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


def test_get_distance():
    print(get_distance((1, 2), (1, 4)))


def extend_array(points, verbose=None):
    n_old = len(points)
    degree = int(ceil(log2(len(points))))
    if verbose:
        print("extend_array: log2(n_points)={} degree={}".format(log2(len(points)), degree))
    n_new = 2 ** degree
    if verbose:
        print("extend_array: n_new=", n_new)
    n_pad = n_new - n_old
    l_pad = int(ceil(n_pad / 2))
    r_pad = n_pad - l_pad
    result = [None] * l_pad + points + [None] * r_pad
    return result, degree


def test_extend_array():
    points = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6)
    ]
    # points = [
    #     (0, 0),
    #     (1, 1),
    #     (2, 2),
    #     (3, 3),
    #     (1, 2)
    # ]
    print(extend_array(points, verbose=True))


def init_sectors(points, verbose=None):
    n_points = len(points)
    indices = list(range(0, n_points, 2))
    if verbose:
        print("init_sectors: idx={}".format(indices))
    distances = [
        get_distance(points[i], points[i + 1])
        for i in indices
    ]

    points_y = []
    for i in range(0, n_points, 2):
        point1 = points[i]
        point2 = points[i + 1]

        if point1 is None or point2 is None:
            points_y.extend([point1, point2])
        elif point2[1] < point1[1]:
            points_y.extend([point2, point1])
        else:
            points_y.extend([point1, point2])

    return distances, points_y


def test_init_sectors():
    # points = [
    #     (1, 2),
    #     (2, 3),
    #     (3, 4),
    #     (4, 5),
    #     (3, 5)
    # ]
    points = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (1, 2)
    ]
    points, n_degree = extend_array(points)
    print("n_degree =", n_degree)
    print("points =", points)
    distances, points_y = init_sectors(points, verbose=True)
    print(distances)
    print(points_y)


def get_intragroup_min(points, begin, end):
    d_min = None
    for i in range(begin, end):
        for j in range(i + 1, end):
            d = get_distance(points[i], points[j])
            if d_min is None or d_min > d:
                d_min = d
    return d_min


def test_get_intragroup_min():
    points = [
        (1, 1),
        (1, 1),
        (1, 3),
        (2, 1),
        (1, 3)
    ]
    print(get_intragroup_min(points, 1, 5))


def get_intergroup_min(points_y, max_x_dist, verbose=None):
    min_d = None
    n_points = len(points_y)
    if verbose:
        print("get_intergroup_min: points_y={}".format(points_y))
        print("get_intergroup_min: max_x_dist={}".format(max_x_dist))
    for ileft in range(n_points):
        for iright in range(ileft + 1, n_points):
            y_dist = get_ydistance(points_y[ileft], points_y[iright])
            dist = get_distance(points_y[ileft], points_y[iright])
            if dist is None or y_dist is None:
                continue
            if y_dist > max_x_dist:
                break
            if verbose:
                print("get_intergroup_min: l_point={} r_point={}".format(points_y[ileft], points_y[iright]))
            if dist is not None:
                if (min_d is None) or (dist < min_d):
                    min_d = dist
    if verbose:
        print("get_intergroup_min: min_dist={}".format(min_d))
    return min_d


def test_get_intergroup_min():
    left = [
        (0, 1),
        (0, 2),
        (1, 1),
        (1, 2)
    ]
    right = [
        (10, 1),
        (10, 2),
        (11, 1),
        (11, 2),
        (0.5, 1)
    ]
    print(get_intergroup_min(left, right))


def merge_y(left, right, verbose=None):
    n_left = len(left)
    n_right = len(right)
    i_left = 0
    i_right = 0
    result = []
    if verbose:
        print("merge_y: left={} right={}".format(left, right))
    while i_left < n_left and i_right < n_right:
        if left[i_left] is None or right[i_right] is None:
            result.append(left[i_left])
            i_left += 1
        elif left[i_left][1] <= right[i_right][1]:
            result.append(left[i_left])
            i_left += 1
        elif left[i_left][1] <= right[i_right][1]:
            result.append(right[i_right])
            i_right += 1
        else:
            result.append(right[i_right])
            i_right += 1
    if i_left < n_left:
        result.extend(left[i_left:])
    elif i_right < n_right:
        result.extend(right[i_right:])
    if verbose:
        print("merge_y: result={}".format(result))
    return result


def test_merge_y():
    left = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 5)
    ]
    right = [
        (2, 2),
        (11, 11),
        (12, 12),
        (13, 13)
    ]
    print(merge_y(right, left, True))


def merge_sectors(points_x, points_y, distances, degree, verbose=None):
    n_dist = len(distances)
    n_points = len(points_y)
    dist_pairs = [distances[i:i + 2] for i in range(0, n_dist, 2)]

    length = 2 ** degree
    distances_new = []
    left_indices = [
        (start, start + length)
        for start in range(0, n_points, 2 * length)
    ]
    right_indices = [
        (start + length, start + 2 * length)
        for start in range(0, n_points, 2 * length)
    ]

    if verbose:
        print("merge_sectors: dist_pairs={}".format(dist_pairs))

    for (l_beg, l_end), (r_beg, r_end), dist_pair in zip(
            left_indices, right_indices, dist_pairs
    ):
        if verbose:
            print("merge_sectors: ypoint_left={} ypoint_left={}".format(points_y[l_beg:l_end], points_y[r_beg:r_end]))
        dist_pair = [x for x in dist_pair if x is not None]
        # TODO: С одной стороны в левой или правой частях может содержаться одна точнка
        # поэтому необходимо искать межгрупповой минимум
        # С другой стороны в отрезке с одной точкой обязательно есть как минимум 1 None
        # Этот None мешает посчитать медиану где слева и спава однаковое 
        if len(dist_pair) == 0:
            distances_new.append(None)
            points_y[l_beg:r_end] = merge_y(points_y[l_beg:l_end], points_y[r_beg:r_end], verbose=verbose)
        elif len(dist_pair) == 1:
            distances_new.append(dist_pair[0])
            points_y[l_beg:r_end] = merge_y(points_y[l_beg:l_end], points_y[r_beg:r_end], verbose=verbose)
        else:
            intra_min = min(dist_pair)
            points_y[l_beg:r_end] = merge_y(points_y[l_beg:l_end], points_y[r_beg:r_end], verbose=verbose)
            mid_point = points_x[(l_beg + r_end) // 2]
            if verbose:
                print("merge_sectors: dist_pair={} mid_point={} idx={}".format(dist_pair, mid_point,
                                                                               (l_beg + r_end) // 2))
            inter_candidates = [
                p for p in points_y[l_beg:r_end]
                if (p is not None) and (get_xdistance(p, mid_point) <= intra_min)
            ]
            inter_min = get_intergroup_min(
                inter_candidates,
                intra_min,
                verbose=verbose
            )
            d_min = min(inter_min, intra_min) if inter_min is not None else intra_min
            if verbose:
                print("merge_sectors: d_min={}".format(d_min))
            distances_new.append(d_min)
    return distances_new, points_y


def test_merge_sectors():
    points_x = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 2),
        (5, 0),
        (6, 1),
        # (7, 1),
        # (8, 0)
    ]
    points_x, n_degree = extend_array(points_x)
    degree = 1
    print("points_x =", points_x)
    dist1, points_y = init_sectors(points_x)
    print("dist1=", dist1)
    dist2, points_y = merge_sectors(points_x, points_y, dist1, degree, verbose=True)
    print("dist2=", dist2)
    dist3, points_y = merge_sectors(points_x, points_y, dist2, degree, verbose=True)
    print("dist3=", dist3)


def get_min_distance(points, verbose=None):
    points_x = sorted(points, key=lambda x: x[0])
    points_x, n_degree = extend_array(points_x)
    # points_y = sorted(points, key=lambda x: x[1])
    # points_y, _ = extend_array(points_y)
    distances, points_y = init_sectors(points_x, verbose=verbose)
    if verbose:
        print("get_min_distance: points_x=", points_x)
        print("get_min_distance: points_y=", points_y)
        print("get_min_distance: init_dist=", distances)
        print()

    for degree in range(1, n_degree):
        distances, points_y = merge_sectors(
            points_x, points_y,
            distances,
            degree, verbose=verbose
        )
        if verbose:
            print("get_min_distance: deg={} dist={}".format(degree, distances))
            print("get_min_distance: points_x=", points_x)
            print("get_min_distance: points_y=", points_y)
            print()
    return distances[0]


def test_get_min_distance():
    points = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (1, 2)
    ]
    dist = get_min_distance(points, verbose=True)
    print("dist = {}".format(dist))


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
        expected, expected_points = get_min_distance_naive(points)
        actual = get_min_distance(points, verbose=True)
        msg = "{}=={} {} {}".format(expected, actual, points, expected_points)
        assert expected == actual, msg


def test01():
    points = [
        (7, 5), (7, 3), (10, 3), (0, 7), (0, 0),
        (5, 10), (3, 7), (3, 3), (0, 4), (6, 7),
        (9, 7), (3, 1), (3, 0), (10, 2), (2, 0),
        (10, 10), (0, 3), (7, 5)
    ]
    dist = get_min_distance(points, verbose=True)
    print("min_distance=", dist)


def test02():
    """
    AssertionError: 0.0==1.0 [(5, 10), (1, 10), (1, 9), (1, 3), (6, 5), (10, 9), (6, 7), (7, 2), (1, 9), (6, 10), (3, 10), (5, 3), (5, 8), (10, 8), (9, 6), (4, 5), (2, 3), (5, 7), (10, 6)]
    ((1, 9), (1, 9))
    :return:
    """
    points = [
        (5, 10), (1, 10), (1, 9), (1, 3), (6, 5),
        (10, 9), (6, 7), (7, 2), (1, 9), (6, 10),
        (3, 10), (5, 3), (5, 8), (10, 8), (9, 6),
        (4, 5), (2, 3), (5, 7), (10, 6)
    ]
    dist = get_min_distance(
        points,
        verbose=True
    )


def test03():
    """
    AssertionError: 1.0==0.0 [(3, 4), (9, 2), (9, 1), (9, 5), (3, 8), (7, 9), (6, 3)] ((9, 2), (9, 1))
    :return:
    """
    points = [(3, 4), (9, 2), (9, 1), (9, 5), (3, 8), (7, 9), (6, 3)]
    dist = get_min_distance(
        points,
        verbose=False
    )
    print("min distance: ", dist)


def test04():
    """
    AssertionError: 1.4142135623730951==0.0 [(4, 2), (9, 2), (8, 3), (9, 6), (4, 0), (3, 4), (7, 5), (6, 9), (5, 3)] ((4, 2), (5, 3))

    :return:
    """
    points = [(4, 2), (9, 2), (8, 3), (9, 6), (4, 0), (3, 4), (7, 5), (6, 9), (5, 3)]
    dist = get_min_distance(
        points,
        verbose=True
    )
    print("min distance: ", dist)


def test05():
    """
    AssertionError: 1.0==1.4142135623730951 [(8, 5), (2, 2), (3, 8), (4, 5), (2, 0), (1, 10), (6, 5), (2, 6), (9, 10), (1, 5), (6, 4), (6, 9)] ((6, 5), (6, 4))
    :return:
    """
    points = [(8, 5), (2, 2), (3, 8), (4, 5), (2, 0), (1, 10), (6, 5), (2, 6), (9, 10), (1, 5), (6, 4), (6, 9)]
    dist = get_min_distance(
        points,
        verbose=False
    )
    print("min distance: ", dist)


def test06():
    """
    AssertionError: 0.0==1.0 [(4, 0), (10, 1), (10, 8), (8, 10), (6, 1), (5, 0), (6, 3), (1, 0), (4, 10), (3, 1), (7, 8), (0, 10), (6, 6), (9, 8), (10, 8), (4, 4), (9, 7), (1, 3)] ((10, 8), (10, 8))
    :return:
    """
    points = [
        (4, 0), (10, 1), (10, 8), (8, 10), (6, 1),
        (5, 0), (6, 3), (1, 0), (4, 10), (3, 1),
        (7, 8), (0, 10), (6, 6), (9, 8), (10, 8),
        (4, 4), (9, 7), (1, 3)
    ]
    dist = get_min_distance(
        points,
        verbose=True
    )
    print("min distance: ", dist, "==", get_min_distance_naive(points))


def test07():
    """
    assert expected == actual, msg
    AssertionError: 0.0==1.0 [(2, 7), (2, 9), (2, 2), (3, 4), (6, 4), (8, 5), (5, 1), (2, 10), (7, 5), (9, 2), (3, 4)] ((3, 4), (3, 4))

    :return:
    """
    points = [(2, 7), (2, 9), (2, 2), (3, 4), (6, 4), (8, 5), (5, 1), (2, 10), (7, 5), (9, 2), (3, 4)]
    dist = get_min_distance(
        points,
        verbose=True
    )
    print("min distance: ", dist, "==", get_min_distance_naive(points))


def test08():
    """
        assert expected == actual, msg
    AssertionError: 1.0==2.23606797749979 [(7, 7), (5, 6), (1, 9), (10, 0), (1, 0), (0, 9)] ((1, 9), (0, 9))
    :return:
    """
    points = [(7, 7), (5, 6), (1, 9), (10, 0), (1, 0), (0, 9)]
    dist = get_min_distance(
        points,
        verbose=True
    )
    print("min distance: ", dist, "==", get_min_distance_naive(points))


def run_interactive():
    n = int(input())
    points = []
    for _ in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
    print(get_min_distance(points, verbose=True))


if __name__ == '__main__':
    # test_merge_sectors()
    # stress_test()
    # run_interactive()
    test08()
