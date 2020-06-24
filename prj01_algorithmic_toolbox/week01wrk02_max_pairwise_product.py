# python3
import random


def expected_max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(
                max_product,
                numbers[first] * numbers[second]
            )
    return max_product


def max_pairwise_product(numbers):
    first_max = None
    second_max = None
    n = len(numbers)

    for i in range(n):
        number = numbers[i]
        if first_max is None:
            first_max = number
        elif first_max <= number:
            second_max = first_max
            first_max = number
        elif second_max is None or second_max < number:
            second_max = number
    return first_max * second_max


def test(n_trials=1000):
    for _ in range(n_trials):
        length = random.randint(5, 20)
        arr = [random.randint(0, 10) for _ in range(length)]
        expected = expected_max_pairwise_product(arr)
        actual = max_pairwise_product(arr)
        msg = "{}=={} {}".format(expected, actual, arr)
        assert expected == actual, msg


if __name__ == '__main__':
    # test()
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
