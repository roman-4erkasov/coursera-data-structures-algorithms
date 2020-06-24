# python3



"""
10
9 7 5 5 2 9 9 9 2 -1
"""
import sys
import threading
import random
from collections import defaultdict, deque


# def compute_height_naive(n, parents):
#     tree = defaultdict([])
#     for node, parent in enumerate(parents):
#         tree[parent].append(node)
#     stack = deque()
#     stack.append((tree[-1][0], 1))
#     max_level = 0
#     while len(stack)>0:
#         node,level = stack.popleft()
#         if level > max_level:
#             max_level = level
#         for child in tree[node]:
#             stack.append((child, level+1))
#     return max_level
#
#
#     # Replace this code with a faster implementation
#     max_height = 0
#     for vertex in range(n):
#         height = 0
#         current = vertex
#         while current != -1:
#             height += 1
#             current = parents[current]
#         max_height = max(max_height, height)
#     return max_height
#
#
def compute_height(n, parents):
    tree = defaultdict(list)
    for node, parent in enumerate(parents):
        tree[parent].append(node)
    stack = deque()
    stack.append((tree[-1][0], 1))
    max_level = 0
    while len(stack)>0:
        node,level = stack.popleft()
        if level > max_level:
            max_level = level
        for child in tree[node]:
            stack.append((child, level+1))
    return max_level


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
