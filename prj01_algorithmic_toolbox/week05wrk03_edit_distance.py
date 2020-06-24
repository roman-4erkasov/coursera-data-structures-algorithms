# Uses python3
"""
The edit distance between two strings is the minimum number of
operations (insertions, deletions, and substitutions of symbols)
to transform one string into another. It is a measure of similarity
of two strings. Edit distance has applications, for example, in
computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance
between two strings.
"""


def edit_distance(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    history = [
        [None for _ in range(n2 + 1)]
        for _ in range(n1 + 1)
    ]
    for col in range(n2 + 1):
        history[0][col] = col
    for row in range(1, n1 + 1):
        history[row][0] = row
    for row in range(1, n1 + 1):
        for col in range(1, n2 + 1):
            history[row][col] = min(
                history[row - 1][col - 1] + int(s1[row - 1] != s2[col - 1]),
                history[row - 1][col] + 1,
                history[row][col - 1] + 1
            )
    # pprint(history)
    return history[n1][n2]


if __name__ == '__main__':
    # edit_distance("distance", "editing")
    # edit_distance("short","ports")
    # edit_distance("ab","ab")
    print(edit_distance(input(),input()))
