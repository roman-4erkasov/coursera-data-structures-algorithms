# Uses python3
"""
Compute the length of a longest common subsequence of three sequences.
"""


from pprint import pprint


def lcs3(s1, s2, s3):
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    history = [
        [[-1] * (n3 + 1) for _ in range(n2+1)]
        for _ in range(n1 + 1)
    ]
    for ax1 in range(0, n1 + 1):
        for ax2 in range(0, n2 + 1):
            for ax3 in range(0, n3 + 1):
                if ax1 == 0 or ax2 == 0 or ax3 == 0:
                    history[ax1][ax2][ax3] = 0
                elif s1[ax1 - 1] == s2[ax2 - 1] == s3[ax3-1]:
                    history[ax1][ax2][ax3] = history[ax1 - 1][ax2 - 1][ax3-1] + 1
                else:
                    history[ax1][ax2][ax3] = max(
                        history[ax1][ax2][ax3-1],
                        history[ax1][ax2-1][ax3],
                        history[ax1][ax2-1][ax3 - 1],
                        history[ax1-1][ax2][ax3],
                        history[ax1-1][ax2][ax3 - 1],
                        history[ax1-1][ax2-1][ax3],
                        history[ax1-1][ax2-1][ax3 - 1]
                    )
    # pprint(history)
    return history[n1][n2][n3]


if __name__ == '__main__':
    _ = input()
    s1 = input().split()
    _ = input()
    s2 = input().split()
    _ = input()
    s3 = input().split()
    print(lcs3(s1, s2, s3))

"""
3
1 2 3
3
2 1 3
3
1 3 5
"""

"""
5
8 3 2 1 7
7
8 2 1 3 8 10 7 
6
6 8 3 1 4 7
"""
