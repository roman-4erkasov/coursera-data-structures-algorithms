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


def


def contains_common_substring(text_1, text_2, pattern_len, primes, x, verbose=False):
    """
    check if text contains pattern

    :param text: text
    :param pattern: substring
    :param primes: list of prime number to generate different hashes
    :param x: argument of polynoms for polyhash function
    :return: True if text cntains substring, otherwise False
    """
    # pattern_len = len(pattern)
    result = False
    # p_hashes = [
    #     polyhash(pattern, prime, x)
    #     for prime in primes
    # ]

    lil_hashes_1 = [
        precompute_hashes(text_1, pattern_len, prime, x)
        for prime in primes
    ]
    lil_hashes_2 = [
        precompute_hashes(text_2, pattern_len, prime, x)
        for prime in primes
    ]

    if verbose:
        print(f"lil_hashes:  {lil_hashes_1})\n  {lil_hashes_2}")

    for hashes_1, hashes_2 in zip(lil_hashes_1, lil_hashes_2):
        index_1 = 0
        index_2 = 0
        for index in range(min(len(text_1), len(text_2))):
            if hashes_1[index] == hashes_2[index]:


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


test_contains()


def get_common_substring(text1, text2):
    # TODO: binary search common substring
    # https://www.quora.com/How-do-I-use-rolling-hash-and-binary-search-to-find-the-longest-common-sub-string
    # https://www.coursera.org/learn/data-structures/discussions/weeks/3/threads/O0VDK7KqEemMUQoC5G__rA
    left = 0
    right = min(len(text1), len(text2))

    while left<right:
        mid = left + (right-left)//2
        if contains()


"""
Suppose you are given 2 string "aaaaa" & "aaa" , maximum it would be possible that smaller string is completely a common substring like in case above and that the idea we use.

So we fix left=0 and right=min(string_A, string_B) = 3

mid = 1 i.e (left+right)/2

Now you try to find substring of length mid using hash. If it succeed, that mean we can at-least have a common substring of length 2,Lets see if we can get better , so in binary search because the substring search returned true left = mid + 1 and doing that we get mid =2, Repeat same process , and you will see SubStringSearch will still return , so again try i.e. now mid =3 and it will again succeed and like that we keep doing until left <=right

SubStringSearch is a function which you have write that compute hash for each substring of length and for each index and then compare with other string 2.

And all this have to be done fast, like you compute hash once and as explained in Problem 3 , you can use it to create hash for other index.


"""

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
prime1 = 1000000007
prime2 = 1000004249
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
