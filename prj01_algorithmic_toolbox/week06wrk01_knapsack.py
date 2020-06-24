# Uses python3
"""
You are given a set of bars of gold and your goal is to take as much gold
as possible into your bag. There is just one copy of each bar and for each
bar you can either take it or not (hence you cannot take a fraction of a bar).

Task. Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊 .
Input Format. The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars
of gold. The next line contains 𝑛 integers 𝑤0 , 𝑤1 , . . . , 𝑤𝑛−1 defining the weights of the bars of gold.
"""
from pprint import pprint


def knapsack(weights, capacity):
    n = len(weights)
    history = [
        [0]*(n + 1)
        for _ in range(capacity+1)
    ]
    for c in range(1, capacity + 1):
        for i in range(1,n+1):
            history[c][i] = history[c][i-1]
            w = weights[i-1]
            if w<=c:
                # pprint(history)
                # print(c,w)
                val = history[c-w][i-1]+w
                if history[c][i]<val:
                    history[c][i] = val
    return history[capacity][n]


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    capacity = arr[0]
    n = arr[1]
    w = [int(x) for x in input().split()]
    print(knapsack(w,capacity))
