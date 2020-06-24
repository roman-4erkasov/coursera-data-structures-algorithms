# Uses python3
"""
Compute the length of a longest common subsequence of three sequences.
"""


from pprint import pprint


def lcs2(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    history = [
        [-1] * (n2 + 1) for _ in range(n1 + 1)
    ]
    for col in range(n2 + 1):
        history[0][col] = 0
    for row in range(1, n1 + 1):
        history[row][0] = 0
    for row in range(1, n1 + 1):
        for col in range(1, n2 + 1):
            if row == 0 or col == 0:
                history[row][col] = 0
            elif s1[row - 1] == s2[col - 1]:
                history[row][col] = history[row - 1][col - 1] + 1
            else:
                history[row][col] = max(
                    history[row][col - 1],
                    history[row - 1][col]
                )
    # pprint(history)
    return history[n1][n2]


if __name__ == '__main__':
    _ = input()
    s1 = input().split()
    _ = input()
    s2 = input().split()
    print(lcs2(s1, s2))
