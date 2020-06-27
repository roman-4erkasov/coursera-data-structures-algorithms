# python3
import random
import sys


class Solver:

    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        return s[a:a + l] == s[b:b + l]


# s = sys.stdin.readline()
# q = int(sys.stdin.readline())
# solver = Solver(s)


# def prefix_hashes(text):
#     """
#     returns precomputed prefix hashes for instant ( O(1) ) getting of subsring hash
#     :param text:
#     :return:
#     """
#     x = 31
#     # x = random.randint(1, 1e9)
#     m1 = 10**9 + 7
#     m2 = 10**9 + 9
#     sum_1 = 0
#     sum_2 = 0
#     hash_1 = [None]*len(text)
#     hash_2 = [None] * len(text)
#     for i, s in enumerate(text):
#         sum_1 = ((sum_1*x+ord(s))%m1+m1)%m1
#         sum_2 = ((sum_2*x+ord(s))%m2+m2)%m2
#         hash_1[i] = sum_1
#         hash_2[i] = sum_1
#     return hash_1б hash_2


def prefix_hashes(text, x, m):
    """
    returns precomputed prefix hashes for instant ( O(1) ) getting of subsring hash
    :param text:
    :return:
    """
    # x = 31
    # x = random.randint(1, 1e9)
    # m1 = 10**9 + 7
    # m2 = 10**9 + 9
    sum_ = 0
    hashes = [None] * len(text)
    for i, s in enumerate(text):
        sum_ = ((sum_ * x + ord(s)) % m + m) % m
        print(f"i={i} sum={sum_}")
        hashes[i] = sum_
    return hashes


# for i in range(q):
#     a, b, l = map(int, sys.stdin.readline().split())
#     print("Yes" if solver.ask(a, b, l) else "No")


m1 = 10 ** 9 + 7
m2 = 10 ** 9 + 9
x = random.randint(1, 10 ** 9)

# print(x)
# print(prefix_hashes("abcd", x, m1))
# print(prefix_hashes("bcd", x, m1))
# print(prefix_hashes("cd", x, m1))
# print(prefix_hashes("d", x, m1))

#
s = sys.stdin.readline()
q = int(sys.stdin.readline())

hashes1 = prefix_hashes(s, x, m1)
hashes2 = prefix_hashes(s, x, m2)

print(x, hashes1, hashes2)

for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())

    x_pow_l = x ** l

    a_h1 = ((hashes1[a + l] - hashes1[a] * x_pow_l) % m1 + m1) % m1
    a_h2 = ((hashes2[a + l] - hashes2[a] * x_pow_l) % m2 + m2) % m2

    b_h1 = ((hashes1[b + l] - hashes1[b] * x_pow_l) % m1 + m1) % m1
    b_h2 = ((hashes2[b + l] - hashes2[b] * x_pow_l) % m2 + m2) % m2
    print(f"a_h1={a_h1} b_h1={b_h1}")
    print(f"a_h2={a_h2} b_h2={b_h2}")
    print("Yes" if (a_h1 == b_h1) and (a_h2 == b_h2) else "No")

# 527676506
# [116, 210474383, 246509207, 136051038, 866976794, 238618898, 480815404, 637693504]
# [116, 210474261, 647851288, 982736736, 503220789, 296243277, 926464738, 480182399]

# 898310178
# [116, 203980034, 368324790, 350623393, 372014145, 474179288, 625472836, 708244548]
# [116, 203979826, 153334771, 190919690, 164059040, 98526092, 445601577, 349354864]

# 138927063
# [97, 475925118, 388836387, 855302209, 42009816]
# [97, 475925092, 644495029, 691229727, 966127185]

# 664408128
# [97, 447588066, 964532525, 844460592]
# [98, 111996188, 91337925]
# [99, 776404317]
# [100]
