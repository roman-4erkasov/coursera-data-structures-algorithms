# python3
import random
import sys


def prefix_hashes(text, x, m):
    """
    returns precomputed prefix hashes for instant ( O(1) ) getting of subsring hash
    :param text:
    :return:
    """
    hashes = [None] * (len(text) + 1)
    hashes[0] = 0
    for i, s in enumerate(text, 1):
        hashes[i] = (hashes[i - 1] * x + ord(s)) % m
    return hashes


m1 = 10 ** 9 + 7
m2 = 10 ** 9 + 9
x = random.randint(1, 10 ** 9)

s = sys.stdin.readline()
q = int(sys.stdin.readline())

hashes1 = prefix_hashes(s, x, m1)
hashes2 = prefix_hashes(s, x, m2)

powers1 = [1] + [0] * len(s)
powers2 = [1] + [0] * len(s)

for i in range(1, len(s)+1):
    powers1[i] = ((powers1[i - 1] * x) % m1 + m1) % m1
    powers2[i] = ((powers2[i - 1] * x) % m2 + m2) % m2

for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())

    # x_pow_l = x ** l

    a_h1 = ((hashes1[a + l] - hashes1[a] * powers1[l]) % m1 + m1) % m1
    a_h2 = ((hashes2[a + l] - hashes2[a] * powers2[l]) % m2 + m2) % m2

    b_h1 = ((hashes1[b + l] - hashes1[b] * powers1[l]) % m1 + m1) % m1
    b_h2 = ((hashes2[b + l] - hashes2[b] * powers2[l]) % m2 + m2) % m2

    print("Yes" if (a_h1 == b_h1) and (a_h2 == b_h2) else "No")

"""
input:
trololo
4
0 0 7
2 4 3
3 5 1
1 3 2

output:
Yes
Yes
Yes
No
"""
