# Uses python3

"""
Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
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


def get_fibonacci_mod_m(n, m, verbose=False):
    lag = [0, 1]
    curr = 0
    pisano = get_pisano_period(m, verbose)
    if verbose: print("pisano=", pisano)
    for _ in range(0, n % pisano):
        curr = (lag[0] % m + lag[1] % m) % m
        lag[1] = lag[0]
        lag[0] = curr
        if verbose: print(lag[1], lag[0], curr)
    return curr


if __name__ == '__main__':
    # print(get_pisano_period(2))
    n, m = map(int, input().split())
    print(get_fibonacci_mod_m(n, m, False))
