# Uses python3
"""
As we already know, a natural greedy strategy for the change problem
does not work correctly for any set of denominations. For example, if
the available denominations are 1, 3, and 4, the greedy algorithm will
change 6 cents using three coins (4 + 1 + 1) while it can be changed
using just two coins (3 + 3). Your goal now is to apply dynamic programming
for solving the Money Change Problem for denominations 1, 3, and 4.
"""


def change(money, verbose=None):
    """
    :return:
    """
    min_num = [0] + [None] * money
    coins = [1, 3, 4]
    for m in range(1, money + 1):
        for coin in coins:
            if verbose:
                print("m={} c={}".format(m, coin))
            if m >= coin:
                n_coins = min_num[m - coin] + 1
                if (min_num[m] is None) or n_coins < min_num[m]:
                    min_num[m] = n_coins
                if verbose:
                    print("min[m]={} min[{}]={} n_coins={}".format(min_num[m], m - coin, min_num[m - coin], n_coins))
    return min_num[m]


if __name__ == '__main__':
    # print(change(5,verbose=False))
    m = int(input())
    print(change(m, verbose=False))
