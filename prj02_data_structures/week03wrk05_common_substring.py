# python3
import random
import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def solve_naive(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i + l] == t[j:j + l]):
                    ans = Answer(i, j, l)
    return ans


def polyhash(string, prime, x):
    # bucket_count = 1000
    ans = 0
    for s in reversed(string):
        ans = ((ans * x + ord(s)) % prime + prime) % prime
    return ans  # % bucket_count


def precompute_hashes(text, pattern_len, prime, x):
    text_len = len(text)
    hashes = [None] * (text_len - pattern_len + 1)
    S = text[text_len - pattern_len:text_len]
    hashes[text_len - pattern_len] = polyhash(S, prime, x)
    y = 1
    for i in range(pattern_len):
        y = ((y * x) % prime + prime) % prime
    for i in range(text_len - pattern_len - 1, -1, -1):
        hashes[i] = ((x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime + prime) % prime
    return hashes


def contains(text, pattern, primes, x, verbose=False):
    """
    check if text contains pattern

    :param text: text
    :param pattern: substring
    :param primes: list of prime number to generate different hashes
    :param x: argument of polynoms for polyhash function
    :return: True if text cntains substring, otherwise False
    """
    pattern_len = len(pattern)
    result = False
    p_hashes = [
        polyhash(pattern, prime, x)
        for prime in primes
    ]

    lil_hashes = [
        precompute_hashes(text, pattern_len, prime, x)
        for prime in primes
    ]

    if verbose:
        print(f"{lil_hashes} {p_hashes}")

    for i in range(0, len(text) - pattern_len + 1):
        eq = True
        for p_hash, hashes in zip(p_hashes, lil_hashes):
            if p_hash != hashes[i]:
                eq = False
                break
        if eq:
            result = True
            break
    return result


def test_contains():
    prime1 = 10 ** 9 + 7
    prime2 = 10 ** 9 + 9
    x = random.randint(1, 10 ** 9)
    text = "ababaxbaba"
    s = "axb"
    print(
        f"{text} contains {s}:"
        f"{contains(text=text,pattern=s,primes=[prime1,prime2],x=x, verbose=True)}"
    )


test_contains()


def get_common_substring(text1, text2):
    # TODO: binary search common substring
    # https://www.quora.com/How-do-I-use-rolling-hash-and-binary-search-to-find-the-longest-common-sub-string
    # https://www.coursera.org/learn/data-structures/discussions/weeks/3/threads/O0VDK7KqEemMUQoC5G__rA
    pass

"""
def _binary_search(self):
    l = 0
    r = min(len(self.s1), len(self.s2))

    while l <= r:
        mid = (l + r) // 2

        if self.compare_hashes(self.s1, self.s2, mid):
            l = mid + 1
        else:
            r = mid - 1

    return r
"""

# prime1 = 10 ** 9 + 7
# prime2 = 10 ** 9 + 9
# x = random.randint(1, 10 ** 9)
#
#
# for line in sys.stdin.readlines():
#     s, t = line.split()
#     ans = solve_naive(s, t)
#     print(ans.i, ans.j, ans.len)

"""
input:
cool toolbox
aaa bb
aabaa babbaab

output:

"""
