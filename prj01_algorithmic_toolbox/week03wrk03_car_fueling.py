# Uses python3
"""
Problem Introduction
You are going to travel to another city that is located 𝑑 miles away from your home city. Your can can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?

Problem Description
Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
Input Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a full tank, and there are gas stations at distances stop1 , stop2 , . . . , stop𝑛 along the way, output the minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.
Constraints. 1≤𝑑≤105.1≤𝑚≤400.1≤𝑛≤300.0<stop1 <stop2 <···<stop𝑛 <𝑑.

Sample 1.
Input:
950
400
4
200 375 550 750
Output:
> 2
The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.

Sample 2.
Input:
10
3
4
1 2 5 9
Output:
> -1
One cannot reach the gas station at point 9 as the previous gas station is too far away.

Sample 3.
Input:
200
250
2
100
150
Output:
> 0
There is no need to refill the tank as the car starts with a full tank and can travel for 250 miles whereas the distance to the destination point is 200 miles.
"""

verbose = False
d = int(input())
m = int(input())
n = int(input())
stops = [int(x) for x in input().split()] + [d]

left = 0
right = 0
prev_stop = 0
n_loads = 0

for stop in stops:
    if verbose: print("stop=", stop, " left=", left, " right=", right, " n_loads=", n_loads)
    if stop - prev_stop>m:
        n_loads = -1
        break
    else:
        if (stop - left) <= m:
            right = stop
        else:
            left = right
            right = stop
            n_loads += 1
    if verbose: print("stop=", stop, " left=", left, " right=", right, " n_loads=", n_loads)
    if verbose: print()
    prev_stop = stop
print(n_loads)
