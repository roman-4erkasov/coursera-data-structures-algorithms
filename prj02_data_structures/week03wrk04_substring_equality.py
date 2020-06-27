# python3

import sys


class Solver:

    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        return s[a:a+l] == s[b:b+l]


# s = sys.stdin.readline()
# q = int(sys.stdin.readline())
# solver = Solver(s)


def prefix_hashes(text):
    """
    returns precomputed prefix hashes for instant ( O(1) ) getting of subsring hash
    :param text:
    :return:
    """
    x = 31
    p = 10**9 + 7
    # p = 10**9 + 9
    sum_ = 0
    hashes = [None]*len(text)
    for i, s in enumerate(text):
        sum_ = ((sum_*x+ord(s))%p+p)%p
        hashes[i] = sum_
    return hashes


print(prefix_hashes("abcd"))
print(prefix_hashes("bcd"))
print(prefix_hashes("cd"))
print(prefix_hashes("d"))

# for i in range(q):
#     a, b, l = map(int, sys.stdin.readline().split())
#     print("Yes" if solver.ask(a, b, l) else "No")


