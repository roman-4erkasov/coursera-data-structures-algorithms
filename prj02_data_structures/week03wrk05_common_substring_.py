# python3

#TODO:  https://iq.opengenus.org/longest-common-substring-using-rolling-hash/
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
    ans = 0
    for s in reversed(string):
        ans = ((ans * x + ord(s)) % prime + prime) % prime
    return ans


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
    s = "a"  # ""axb"
    print(
        f"{text} contains {s}:"
        f"{contains(text=text,pattern=s,primes=[prime1,prime2],x=x, verbose=True)}"
    )


class IntDict:
    """
    Hash Table that implemetns dict of integers
    """

    bucket_count = 100_000

    def __init__(self, prime, values=None):
        self.prime = prime
        self.a = random.randint(1, self.bucket_count - 1)
        self.b = random.randint(0, self.bucket_count - 1)
        self.data = [[] for _ in range(self.bucket_count)]

    @staticmethod
    def __safe_modulo(value, modulus):
        """
        modulo operation that prevents from negative hashes
        :param value:
        :param modulus:
        :return: remainder of modulo operation
        """
        return (value % modulus + modulus) % modulus

    def get_hash(self, value):
        """
        hash function from Universal Family
        :param value: integer value
        :return: hash of the integer
        """
        result = self.__safe_modulo(self.a * value + self.b, self.prime)
        return self.__safe_modulo(result, self.bucket_count)

    def exists(self, item: int):
        result = False
        h = self.get_hash(item)
        for k, v in self.data[h]:
            if item == k:
                result = True
        return result

    def __getitem__(self, item: int):
        h = self.get_hash(item)
        result = None
        for i, (k, v) in enumerate(self.data[h]):
            if item == k:
                result = v
                break
        return result

    def __setitem__(self, key: int, value):
        h = self.get_hash(key)
        found = False
        for i, (k, v) in enumerate(self.data[h]):
            if key == k:
                found = True
                self.data[h][i] = [key, value]

        if not found:
            self.data[h].append([key, value])

    def __str__(self):
        return "{" + " ".join([str(i) + ":" + str(x) for i, x in enumerate(self.data) if x]) + "}"


def test_int_set():
    h_table_1 = IntDict(prime_1)
    h_table_1[3] = 1

    print(h_table_1)


def get_common_substring(text_1, text_2, pattern_len, prime_1, prime_2, x, verbose=False):
    """
    checks if text contains pattern
    :param text_1:
    :param text_2:
    :param pattern_len:
    :param prime_1:
    :param prime_2:
    :param x:
    :param verbose:
    :return:
    """

    swap = False

    if len(text_1)<len(text_2):
        text_1, text_2 = text_2, text_1
        swap = True

    result = None
    prime_3 = 1_000_000_007

    hashes_t1_p1 = precompute_hashes(text_1, pattern_len, prime_1, x)
    hashes_t1_p2 = precompute_hashes(text_1, pattern_len, prime_2, x)

    hashes_t2_p1 = precompute_hashes(text_2, pattern_len, prime_1, x)
    hashes_t2_p2 = precompute_hashes(text_2, pattern_len, prime_2, x)

    # primes that differ from prime of hash and differ from each other
    hash_set_p1 = IntDict(prime=prime_2)
    hash_set_p2 = IntDict(prime=prime_3)
    for i in range(len(hashes_t2_p1)):
        hash_set_p1[hashes_t2_p1[i]] = i
        hash_set_p2[hashes_t2_p2[i]] = i

    if verbose:
        print(f"s1p1={hashes_t1_p1} s2p1={hash_set_p1}")
        print(f"s1p2={hashes_t1_p2} s2p1={hash_set_p2}")

    for idx, (hash_p1, hash_p2) in enumerate(zip(hashes_t1_p1, hashes_t1_p2)):
        if hash_set_p1.exists(hash_p1) and hash_set_p2.exists(hash_p2):
            result = idx, hash_set_p1[hash_p1], pattern_len
            break
    if swap:
        a, b, c = result
        result = a,c,b
    return result


def get_longest_common_substring(text_1, text_2, verbose=False):
    prime_1 = 1_000_000_007
    prime_2 = 1_000_004_249
    x = random.randint(1, 10 ** 9)
    left = 0
    right = min(len(text_1), len(text_2))
    while left <= right:
        mid = left + (right - left) // 2
        res = get_common_substring(
            text_1=text_1, text_2=text_2,
            pattern_len=mid,
            prime_1=prime_1, prime_2=prime_2,
            x=x,
            verbose=verbose
        )
        if res is None:
            right = mid - 1
        else:
            left = mid + 1
    if right > 0:
        result = get_common_substring(
            text_1=text_1, text_2=text_2,
            pattern_len=right,
            prime_1=prime_1, prime_2=prime_2,
            x=x,
            verbose=verbose
        )
    elif right == 0:
        result = (0, 0, 0)
    else:
        msg = f"left={left} mid={mid} right={right}"
        raise Exception(msg)
    return result


def test_get_longest_common_substring():
    # text_1 = "aaabaa"
    # text_2 = "baabbb"

    # text_1 = "cool"
    # text_2 = "toolbox"

    # text_1 = "aaa"
    # text_2 = "bb"

    # text_1 = "aabaa"
    # text_2 = "babbaab"

    text_1 = "voteforthegreatalbaniaforyou"
    text_2 = "choosethegreatalbanianfuture"

    res1 = get_longest_common_substring(text_1, text_2)
    print(text_1, text_2)
    print(res1)  # , res2)


def main_naive():
    # print("Print two string separated by space to continue or print Ctrl+D to exit...")
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve_naive(s, t)
        print(ans.i, ans.j, ans.len)


def main():
    # print("Print two string separated by space to continue or print Ctrl+D (Cmd+D for Mac) to exit...")
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = get_longest_common_substring(s, t)
        print(" ".join([str(x) for x in ans]))


if __name__ == '__main__':
    main()

"""
input:
cool toolbox
aaa bb
aabaa babbaab

output:
1 1 3
0 1 0
0 4 3
"""
