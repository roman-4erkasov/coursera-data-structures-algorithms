# Uses python3
"""
Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
Constraints. 1≤𝑛≤103,0≤𝑊 ≤2·106;0≤𝑣𝑖 ≤2·106,0<𝑤𝑖 ≤2·106 forall1≤𝑖≤𝑛.Allthe numbers are integers.
Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference between the answer of your program and the optimal value should be at most 10−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
Sample 1.
Input:
> 3 50
> 60 20
> 100 50
> 120 30
Output:
> 180.0000
To achieve the value 180, we take the first item and the third item into the bag.
Sample 2.
Input:
1 10
500 30
Output:
> 166.6667
Here, we just take one third of the only available item.
"""


def max_value(items:list, W):
    items.sort(key=lambda x: x[0], reverse=True)
    value = 0
    for sgfce, w, v in items:
        if W == 0:
            break
        elif w < W:
            value += v
            W -= w
        else:
            value += W * sgfce
            W = 0
    return value


inp = list(input().split())
assert len(inp) == 2

N = int(inp[0])
W = float(inp[1])

items = []
for _ in range(N):
    inp = list(input().split())
    v = float(inp[0])  # value
    w = float(inp[1])  # weight
    sgfce = v / w  # significance
    items.append((sgfce, w, v))
print(max_value(items, W))
