# Uses python3
import re
from pprint import pprint


def get_operands(string):
    return re.findall(pattern="\d+", string=string)


def get_operations(string):
    return re.findall(pattern="[\+\-\*\/]", string=string)


def parse_expresiion(string):
    return get_operands(string), get_operations(string)


def get_min_max(row, col, operations, m_min, m_max):
    min_v = None
    max_v = None

    for k in range(row, col):
        a = eval(str(m_max[row][k] + operations[k] + m_max[k + 1][col]))
        b = eval(str(m_max[row][k] + operations[k] + m_min[k + 1][col]))
        c = eval(str(m_min[row][k] + operations[k] + m_max[k + 1][col]))
        d = eval(str(m_min[row][k] + operations[k] + m_min[k + 1][col]))
        x = min(a, b, c, d)
        if min_v is None or x < min_v:
            min_v = x
        x = max(a, b, c, d)
        if max_v is None or x > max_v:
            max_v = x
    return str(min_v), str(max_v)


def maximize_naive(operands, operations):
    pass


def maximize(operands, operations):
    n = len(operands)
    m_max = [[None] * n for _ in range(n)]
    m_min = [[None] * n for _ in range(n)]

    for i in range(n):
        m_max[i][i] = operands[i]
        m_min[i][i] = operands[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m_min[i][j], m_max[i][j] = get_min_max(i, j, operations, m_min, m_max)
    return m_max[0][n-1]


if __name__ == '__main__':
    # pprint(maximize(*parse_expresiion("5-8+7*4-8+9")))
    expression = input()
    print(maximize(*parse_expresiion(expression)))
