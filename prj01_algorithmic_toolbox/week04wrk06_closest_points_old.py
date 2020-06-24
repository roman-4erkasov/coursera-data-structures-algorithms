# Uses python3
import random
from math import sqrt


def get_closest_points_naive(points):
    closest_points = None
    min_distance = None
    n = len(points)
    points_ext = [
        {
            "x": p[0],
            "y": p[1]
        }
        for p in points
    ]
    for i in range(n):
        for j in range(i + 1, n):
            point2 = points_ext[j]
            point1 = points_ext[i]
            distance = get_distance(point1, point2)
            if min_distance is None or distance < min_distance:
                min_distance = distance
                closest_points = (point1, point2)
    return min_distance, closest_points


def get_distance(point1, point2):
    dist = sqrt(
        (point2["x"] - point1["x"]) ** 2 + (point2["y"] - point1["y"]) ** 2
    )
    return dist

def get_xdistance(point1, point2):
    dist = sqrt(
        (point2["x"] - point1["x"]) ** 2 + (point2["y"] - point1["y"]) ** 2
    )
    return dist

def get_intra_min(points):
    """
    Returns minimal distance from the list of the points
    :param points: list of the points
    :return: minimal distans
    """
    n = len(points)
    if len(points) > 1:
        min_dist = None
        for idx1 in range(n):
            for idx2 in range(idx1 + 1, n):
                dist = get_distance(
                    points[idx1],
                    points[idx2]
                )
                if (min_dist is None) or (dist < min_dist):
                    min_dist = dist
        return min_dist
    elif len(points) == 1:
        return None
    else:
        msg = "Unexpected num of points: {}".format(points)
        raise Exception(msg)


def get_inter_min(left_sector, right_sector, verbose=None):
    if verbose:
        print(
            "get_inter_min[start]: left={} right={}".format(
                left_sector,
                right_sector
            )
        )
    min_dist = None
    for idx in range(1, 7):
        left_bound = -7+idx
        right_bound = idx
        if verbose:
            print(
                "get_inter_min[idx={}]: left={} right={}".format(
                    idx,
                    left_sector[left_bound:],
                    right_sector[:right_bound]
                )
            )
        for left in left_sector[left_bound:]:
            for right in right_sector[:right_bound]:
                dist = get_distance(left, right)
                if verbose:
                    print(
                        "get_inter_min: p_left={} p_right={} d={} min={}".format(
                            left, right, dist, min_dist
                        )
                    )
                condition = (min_dist is None) \
                    or ((dist is not None) and (dist < min_dist))
                if condition:
                    min_dist = dist
    return min_dist


def merge_sectors(sectors, array, verbose=None):
    n = len(sectors)
    result = []
    for pair in [sectors[i:i + 2] for i in range(0, n, 2)]:
        pair_len = len(pair)
        if pair_len == 1:
            result.append(pair[0])
        elif pair_len == 2:
            left_sector = pair[0]
            right_sector = pair[1]
            left_arr = array[left_sector["left"]:(left_sector["right"]+1)]
            right_arr = array[right_sector["left"]:(right_sector["right"]+1)]
            min_candidates = [
                ("left",get_intra_min(left_arr)),
                ("right", get_intra_min(right_arr)),
                ("inter", get_inter_min(left_arr, right_arr, verbose=verbose))
            ]
            if verbose:
                print("merge_sectors: min_candidates =", min_candidates)
            min_values = [v for k, v in min_candidates if v is not None]
            min_dist = min(*min_values)
            sector = {
                "left": left_sector["left"],
                "right": right_sector["right"],
                "min_dist": min_dist
            }
            result.append(sector)
        else:
            raise Exception("invalid pair" + str(pair))
    return result


def init_sectors(points):
    n_points = len(points)
    result = []
    for i in range(0, n_points, 2):
        left_bound = i
        right_bound = min(n_points - 1, i + 1)
        min_dist = None
        if left_bound < right_bound:
            min_dist = get_distance(
                points[left_bound],
                points[right_bound]
            )
        elif left_bound > right_bound:
            err_msg = "left={} right={}".format(
                left_bound,
                right_bound
            )
            raise Exception(err_msg)
        result.append({
            "min_dist": min_dist,
            "left": left_bound,
            "right": right_bound
        })
    return result


def get_closest_points(points, verbose=None):
    n_points = len(points)
    if n_points == 0:
        return None
    points_ext = [
        {
            "x": p[0],
            "y": p[1]
        }
        for p in points
    ]
    y_sorted = sorted(points_ext, key=lambda p: p["y"])
    y_sorted = [
        {
            "x": p["x"],
            "y": p["y"],
            "y_index": idx
        }
        for idx, p in enumerate(y_sorted)
    ]

    x_sorted = sorted(y_sorted, key=lambda p: p["x"])

    sectors = init_sectors(x_sorted)
    while len(sectors) > 1:
        sectors = merge_sectors(sectors, x_sorted, verbose=verbose)
    min_dist = sectors[0]["min_dist"]
    return min_dist


def test_get_distance():
    point1 = {"x":1,"y":2}
    point2 = {"x":1,"y":0}
    print(get_distance(point1, point2))


def test_get_intra_min():
    points = [
        (0, 0),
        (3, 4),
        (1, 0)
    ]
    points_ext = [{"x": p[0],"y": p[1]} for p in points]
    print(get_intra_min(points_ext))


def test_get_inter_min():
    points = [
        (0, 0),
        (3, 4),
        (1, 0)
    ]
    points_ext = [
        {
            "x": p[0],
            "y": p[1]
        }
        for p in points
    ]
    y_sorted = sorted(points_ext, key=lambda p: p["y"])
    y_sorted = [
        {
            "x": p["x"],
            "y": p["y"],
            "y_index": idx
        }
        for idx, p in enumerate(y_sorted)
    ]
    x_sorted = sorted(y_sorted, key=lambda p: p["x"])

    sectors = init_sectors(x_sorted)
    left_arr = x_sorted[sectors[0]["left"]:(sectors[0]["right"]+1)]
    right_arr = x_sorted[sectors[1]["left"]:(sectors[1]["right"]+1)]
    print("sectors=",sectors)
    print(get_inter_min(left_arr,right_arr,verbose=True))


def test_merge_sectors():
    points = [
        (0, 0),
        (3, 4),
        (1, 0)
    ]
    points_ext = [
        {
            "x": p[0],
            "y": p[1]
        }
        for p in points
    ]
    y_sorted = sorted(points_ext, key=lambda p: p["y"])
    y_sorted = [
        {
            "x": p["x"],
            "y": p["y"],
            "y_index": idx
        }
        for idx, p in enumerate(y_sorted)
    ]
    x_sorted = sorted(y_sorted, key=lambda p: p["x"])
    sectors = init_sectors(x_sorted)
    print("sectors=",sectors)
    sectors2 = merge_sectors(sectors, x_sorted, verbose=True)
    print("sectors=",sectors2)


def test_get_closest_points():
    points = [
        (0, 0),
        (3, 4),
        (1, 0)
    ]
    print(get_closest_points(points))


def test1():
    points = [
        (0, 0),
        (3, 4)
    ]
    print(get_closest_points_naive(points))
    print(get_closest_points(points))


def test2():
    points = [
        (7, 7),
        (1, 100),
        (4, 8),
        (7, 7),
        (1, 1)
    ]
    print(get_closest_points_naive(points))
    print(get_closest_points(points))


def test3():
    """
    AssertionError: 1.4142135623730951==2.0 [(9, 6), (10, 3), (7, 0), (6, 1), (6, 4), (1, 4), (1, 7), (3, 4)]
    :return:
    """
    points = [
        (9, 6), (10, 3), (7, 0), (6, 1),
        (6, 4), (1, 4), (1, 7), (3, 4)
    ]
    print(get_closest_points_naive(points))
    print(get_closest_points(points, verbose=False))

def test4():
    """
    AssertionError: 1.0==2.0 [(3, 5), (10, 4), (8, 0), (5, 7), (6, 1), (0, 0), (8, 4), (5, 1)]
    """
    points = [
        (3, 5), (10, 4), (8, 0), (5, 7),
        (6, 1), (0, 0), (8, 4), (5, 1)
    ]
    print(get_closest_points_naive(points))
    print(get_closest_points(points, verbose=True))


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
        expected, expected_points = get_closest_points_naive(points)
        actual = get_closest_points(points)
        msg = "{}=={} {}".format(expected, actual, points)
        assert expected == actual, msg


def test5():
    points = []
    print(get_closest_points_naive(points))
    print(get_closest_points(points, verbose=False))


def run_interactive():
    n = int(input())
    points = []
    for _ in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
    print(get_closest_points(points))


if __name__ == '__main__':
    # test_get_distance()
    # test_get_intra_min()
    # test_get_inter_min()
    # test_merge_sectors()
    # test_get_closest_points()
    # test5()
    stress_test()
    # run_interactive()
