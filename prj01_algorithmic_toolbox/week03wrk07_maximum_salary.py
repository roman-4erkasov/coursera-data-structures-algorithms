# Uses python3
"""
7 Maximum Salary

Problem Introduction
As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number. How can you do this?
In the lectures, we considered the following algorithm for composing the largest number out of the given single-digit numbers.

LargestNumber(Digits): answer ← empty string while Digits is not empty:
maxDigit ← −∞ for digit in Digits:
if digit ≥ maxDigit: maxDigit ← digit
append maxDigit to answer
remove maxDigit from Digits return answer
Unfortunately, this algorithm works only in case the input consists of single-digit numbers. For example, for an input consisting of two integers 23 and 3 (23 is not a single-digit number!) it returns 233, while the largest number is in fact 323. In other words, using the largest number from the input as the first number is not a safe move.
Your goal in this problem is to tweak the above algorithm so that it works not only for single-digit numbers, but for arbitrary positive integers.
Problem Description
Task. Compose the largest number out of a set of integers.
Input Format. The first line of the input contains an integer 𝑛. The second line contains integers
𝑎1,𝑎2,...,𝑎𝑛.
Constraints. 1≤𝑛≤100;1≤𝑎𝑖 ≤103 forall1≤𝑖≤𝑛.
Output Format. Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.

Sample 1.
Input:
2
21 2
Output:
221
Note that in this case the above algorithm also returns an incorrect answer 212.

Sample 2.
Input:
5
9 4 6 1 9
Output:
99641
In this case, the input consists of single-digit numbers only, so the algorithm above computes the right answer.
Sample 3.
Input:
3
23 39 92
Output:
923923
As a coincidence, for this input the above algorithm produces the right result, though the input does not have any single-digit numbers.
What To Do
Interestingly, for solving this problem, all you need to do is to replace the check digit ≥ maxDigit with a call IsGreaterOrEqual(digit,maxDigit) for an appropriately implemented function IsGreaterOrEqual. For example, IsGreaterOrEqual(2, 21) should return True.
Need Help?
Ask a question or see the questions asked by other learners at this forum thread.
"""

N = int(input())
arr = [str(x) for x in input().split()]


def max_number(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            trial_i = int(arr[i] + arr[j])
            trial_j = int(arr[j] + arr[i])
            if trial_j > trial_i:
                arr[i], arr[j] = arr[j], arr[i]
    return "".join(arr)


print(max_number(arr))
