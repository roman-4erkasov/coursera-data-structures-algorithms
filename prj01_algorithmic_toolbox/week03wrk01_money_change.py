# Uses python3
"""
Problem Description
Task. The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer 𝑚.
Constraints. 1 ≤ 𝑚 ≤ 103.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
"""


def num_of_coins(money, denominations=[1, 5, 10]):
    n_coins = 0
    denominations.sort(reverse=True)
    for denomination in denominations:
        if money == 0:
            break
        elif money >= denomination:
            n_coins += money // denomination
            money %= denomination
    return n_coins


money = int(input())
print(num_of_coins(money))
