# Uses python3
"""
4 Maximum Advertisement Revenue
Problem Introduction
You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up 𝑛 slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

Problem Description
Task. Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗) such that the sum of their products is maximized.
Input Format. The first line contains an integer 𝑛, the second one contains a sequence of integers 𝑎1,𝑎2,...,𝑎𝑛, the third one contains a sequence of integers 𝑏1,𝑏2,...,𝑏𝑛.
Constraints. 1≤𝑛≤103;−105 ≤𝑎𝑖,𝑏𝑖 ≤105 forall1≤𝑖≤𝑛.

Output Format.
Output the maximum value of ∑︀ 𝑎𝑖𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of
 𝑏1,𝑏2,...,𝑏𝑛.

Sample 1.
Input:
1
23
39
Output:
897

897 = 23 · 39.

Sample 2.
Input:
3
1 3 -5
-2 4 1
Output:
23

23 = 3 · 4 + 1 · 1 + (−5) · (−2).

Need Help?
Ask a question or see the questions asked by other learners at this forum thread.
"""

N = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort(reverse=True)
b.sort(reverse=True)
result = sum(pair[0]*pair[1] for pair in zip(a, b))
print(result)