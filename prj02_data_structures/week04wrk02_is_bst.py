#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if len(tree) == 0:
        return True
    else:
        idx = 0
        val = tree[idx][0]
        result_left = True
        result_right = True
        if tree[idx][1] >= 0:
            result_left = node_rec(tree[idx][1], tree, None, val)
        if tree[idx][2] >= 0:
            result_right = node_rec(tree[idx][2], tree, val, None)
        result = result_left and result_right
        return result


def node_rec(idx, tree, minimum, maximum):
    val = tree[idx][0]
    cond_both = \
        minimum is not None and \
        maximum is not None and \
        minimum < val < maximum
    cond_min = \
        minimum is not None and \
        maximum is None and \
        minimum < val
    cond_max = \
        minimum is None and \
        maximum is not None and \
        val < maximum
    if cond_both or cond_min or cond_max:
        result_left = True
        result_right = True
        if tree[idx][1] >= 0:
            result_left = node_rec(tree[idx][1], tree, minimum, val)
        if tree[idx][2] >= 0:
            result_right = node_rec(tree[idx][2], tree, val, maximum)
        result = result_left and result_right
        return result
    else:
        return False


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

"""
3
2 1 2
1 -1 -1
3 -1 -1

CORRECT
"""

"""
3
1 1 2
2 -1 -1
3 -1 -1

INCORRECT
"""

"""
0

CORRECT
"""

"""
5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1

CORRECT
"""

"""
7
4 1 2
2 3 4
6 5 6
1 -1 -1
3 -1 -1
5 -1 -1
7 -1 -1

CORRECT
"""

"""
4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1

INCORRECT
"""
