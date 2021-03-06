# python3


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def polyhash(string, x, prime):
    # bucket_count = 1000
    ans = 0
    for s in reversed(string):
        ans = ((ans * x + ord(s)) % prime + prime) % prime
    return ans #% bucket_count


def precompute_hashes(text, pattern_len, prime, x):
    text_len = len(text)
    hashes = [None] * (text_len - pattern_len + 1)
    S = text[text_len - pattern_len:text_len]
    hashes[text_len - pattern_len] = polyhash(S, x, prime)
    y = 1
    for i in range(pattern_len):
        y = ((y * x) % prime + prime) % prime
    for i in range(text_len - pattern_len - 1, -1, -1):

        hashes[i] = ((x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime + prime) % prime
    return hashes


def get_occurrences(pattern, text):
    """
    returns positions of occurensies using Rabin-Karp algorithm
    :param pattern: substring
    :param text: text
    :return: positions of occurencies
    """
    x = 263
    prime = 1000000007
    pattern_len = len(pattern)
    result = []
    phash = polyhash(pattern, x, prime)
    hashes = precompute_hashes(text, pattern_len, prime, x)
    # print([ord(x) for x in pattern])
    # print([ord(x) for x in text])
    # print(hashes)
    for i in range(0, len(text) - pattern_len+1):
        # print(f"{pattern}={text[i:i + pattern_len]} {phash}={hashes[i]}")

        if phash != hashes[i]:
            continue
        elif pattern == text[i:i + pattern_len]:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

"""
input:
aba
abacaba

output:
0 4
"""

"""
input:
Test
testTesttesT

output:
4
"""

"""
input:
aaaaa
baaaaaaa

output:
1 2 3
"""
