# python3

import sys, threading
from queue import deque

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        # recursive version
        # in_order_rec(0, self.result, self.key, self.left, self.right)

        # iterative version
        curr = 0
        buff = deque()
        while curr >= 0 or buff:
            while curr >= 0:
                buff.append(curr)
                curr = self.left[curr]
            curr = buff.pop()
            self.result.append(self.key[curr])
            curr = self.right[curr]

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        # recursive version
        # pre_order_rec(0, self.result, self.key, self.left, self.right)

        # iterative version
        buff = deque()
        curr = 0
        while curr >= 0 or buff:
            while curr >= 0:
                self.result.append(self.key[curr])
                buff.append(curr)
                curr = self.left[curr]
            curr = buff.pop()
            curr = self.right[curr]

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        # recursive version
        # post_order_rec(0, self.result, self.key, self.left, self.right)

        # iterative version
        buff1 = deque([0])
        buff2 = deque()
        while buff1:
            node = buff1.pop()
            buff2.append(node)
            if self.left[node] >= 0:
                buff1.append(self.left[node])
            if self.right[node] >= 0:
                buff1.append(self.right[node])
        while buff2:
            idx = buff2.pop()
            self.result.append(self.key[idx])

        return self.result


def in_order_rec(idx, result, keys, left, right):
    if left[idx] >= 0:
        in_order_rec(left[idx], result, keys, left, right)
    result.append(keys[idx])
    if right[idx] >= 0:
        in_order_rec(right[idx], result, keys, left, right)


def pre_order_rec(idx, result, keys, left, right):
    result.append(keys[idx])
    if left[idx] >= 0:
        pre_order_rec(left[idx], result, keys, left, right)
    if right[idx] >= 0:
        pre_order_rec(right[idx], result, keys, left, right)


def post_order_rec(idx, result, keys, left, right):
    if left[idx] >= 0:
        post_order_rec(left[idx], result, keys, left, right)
    if right[idx] >= 0:
        post_order_rec(right[idx], result, keys, left, right)
    result.append(keys[idx])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()

"""
input:
5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1
output:
1 2 3 4 5
4 2 1 3 5
1 3 2 5 4
"""

"""
input:
0
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1
output:
50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0
"""