# Uses python3
"""
The goal in this problem is to find the last digit of a sum of the first 𝑛 Fibonacci numbers.
"""


def get_pisano_period(m, verbose=True):
    prev = 0  # F[0]
    curr = 1  # F[1]
    n = 0
    while (not (prev == 0 and curr == 1)) or n <= 0:
        prev, curr = curr % m, (prev % m + curr % m) % m
        n += 1
        if verbose: print("pisano: n=", n, "prev=", prev, "curr=", curr)
    return n


def get_fibonacci_sum_mod_10(n, verbose=False):
    m = 10
    lag = [0, 1]
    curr = None
    pisano = get_pisano_period(m, verbose)
    if verbose: print("pisano=", pisano)
    s = 0
    for _ in range(0, n % pisano):
        curr = (lag[0] % m + lag[1] % m) % m
        lag[1] = lag[0]
        lag[0] = curr

        s += curr % m
        s %= m
        if verbose: print(lag[1], lag[0], curr, s)
    return s


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_sum_mod_10(n))
