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
        if values is not None:
            self.multiple_add(values)

    @staticmethod
    def __safe_modulo(value, modulus):
        """
        modulo operation that prevents from negative hashes
        :param value:
        :param modulus:
        :return: remainder of modulo operation
        """
        return (value % modulus + modulus) % modulus

    def __hash(self, value):
        """
        hash function from Universal Family
        :param value: integer value
        :return: hash of the integer
        """
        result = self.__safe_modulo(self.a * value + self.b, self.prime)
        return self.__safe_modulo(result, self.bucket_count)

    def exists(self, item: int):
        h = self.__hash(item)
        return item in self.data[h]

    def __getitem__(self, item: int):
        h = self.__hash(item)
        result = None
        for i, (k, v) in enumerate(self.data[h]):
            if item == k:
                result = v
        return result

    def __setitem__(self, key:int, value):
        h = self.__hash(value)
        found = False
        for i, pair in enumerate(self.data[h]):
            k, v = pair
            if key == k:
                found = True
                self.data[h][i] = v
        if not found:
            self.data[h].append((key, value))

    def add(self, value):
        h = self.__hash(value)
        if value not in self.data[h]:
            self.data[h].append(value)

    def multiple_add(self, values):
        for value in values:
            self.add(value)

    def __str__(self):
        return self.data


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

    result = None
    prime_3 = 1_000_000_007

    if len(text_1)>len(text_2):
        text_1, text_2 = text_2, text_1

    lil_t1_p1 = precompute_hashes(text_1, pattern_len, prime_1, x)
    lil_t1_p2 = precompute_hashes(text_1, pattern_len, prime_2, x)

    lil_t2_p1 = precompute_hashes(text_2, pattern_len, prime_1, x)
    lil_t2_p2 = precompute_hashes(text_2, pattern_len, prime_2, x)

    # primes that differ from prime of hash and differ from each other
    hash_set_p1 = IntDict(prime=prime_2)
    hash_set_p2 = IntDict(prime=prime_3)
    for i in range(len(lil_t2_p1)):
        hash_set_p1[i] = lil_t2_p1[i]
        hash_set_p2[i] = lil_t2_p2[i]

    for idx,(hash_p1, hash_p2) in enumerate(zip(lil_t1_p1, lil_t1_p2)):
        if hash_set_p1.exists(hash_p1) and hash_set_p2.exists(hash_p2):
            result = idx
            break
    return result




prime_1 = 1_000_000_007
prime_2 = 1_000_004_249

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
x = random.randint(1, 10 ** 9)

res = get_common_substring(text_1="aaabaa", text_2="baabbb", pattern_len=1, prime_1=prime_1, prime_2=prime_2, x=x, verbose=False)
print(res)

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
