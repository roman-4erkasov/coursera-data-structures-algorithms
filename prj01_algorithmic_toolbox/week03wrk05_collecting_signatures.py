# Uses python3
"""
Problem: Collecting Signatures (Covering Segments by Points)
Problem Introduction
You are responsible for collecting signatures from all tenants of a certain build- ing. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as possible.
The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each segment contains at least one marked point.

Problem Description
Task. Given a set of 𝑛 segments {[𝑎0,𝑏0],[𝑎1,𝑏1],...,[𝑎𝑛−1,𝑏𝑛−1]} with integer coordinates on a line, find the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖,𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such that𝑎𝑖 ≤𝑥≤𝑏𝑖.
Input Format. The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines contains two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th segment.
Constraints. 1≤𝑛≤100;0≤𝑎𝑖 ≤𝑏𝑖 ≤109 forall0≤𝑖<𝑛.
Output Format. Output the minimum number 𝑚 of points on the first line and the integer coordinates of 𝑚 points (separated by spaces) on the second line. You can output the points in any order. If there are many such sets of points, you can output any set. (It is not difficult to see that there always exist a set of points of the minimum size such that all the coordinates of the points are integers.)

Sample 1.
Input:
3
1 3
2 5
3 6
Output:
1
3
In this sample, we have three segments: [1,3],[2,5],[3,6] (of length 2,3,3 respectively). All of them contain the point with coordinate 3: 1 ≤ 3 ≤ 3, 2 ≤ 3 ≤ 5, 3 ≤ 3 ≤ 6.

Sample 2.
Input:
4
4 7
1 3
2 5
5 6
Output:
2
3 6

Sample 3
Input:
100
41 42
52 52
63 63
80 82
78 79
35 35
22 23
31 32
44 45
81 82
36 38
10 12
1 1
23 23
32 33
87 88
55 56
69 71
89 91
93 93
38 40
33 34
14 16
57 59
70 72
36 36
29 29
73 74
66 68
36 38
1 3
49 50
68 70
26 28
30 30
1 2
64 65
57 58
58 58
51 53
41 41
17 18
45 46
4 4
0 1
65 67
92 93
84 85
75 77
39 41
15 15
29 31
83 84
12 14
91 93
83 84
81 81
3 4
66 67
8 8
17 19
86 87
44 44
34 34
74 74
94 95
79 81
29 29
60 61
58 59
62 62
54 56
58 58
79 79
89 91
40 42
2 4
12 14
5 5
28 28
35 36
7 8
82 84
49 51
2 4
57 59
25 27
52 53
48 49
9 9
10 10
78 78
26 26
83 84
22 24
86 87
52 54
49 51
63 64
54 54

Output:
43
1 4 5 8 9 10 14 15 18 23 26 28 29 30 32 34 35 36 40 41 44 46 49 52 54 56 58 61 62 63 65 67 70 74 77 78 79 81 84 87 91 93 95

The second and the third segments contain the point with coordinate 3 while the first and the fourth segments contain the point with coordinate 6. All the four segments cannot be covered by a single point, since the segments [1, 3] and [5, 6] are disjoint.
Need Help?

Ask a question or see the questions asked by other learners at this forum thread. Solution
A detailed solution (with Python code) for this challenge is covered in the companion MOOCBook. We strongly encourage you to do your best to solve the challenge yourself before looking into the book! There are at least three good reasons for this.
∙ By solving this challenge, you practice solving algorithmic problems similar to those given at technical interviews.
∙ The satisfaction and self confidence that you get when passing the grader is priceless =)
∙ Even if you fail to pass the grader yourself, the time will not be lost as you will better understand the
solution from the book and better appreciate the beauty of the underlying ideas.
"""

verbose = False
N = int(input())
periods = []
for idx in range(N):
    inp = [int(x) for x in input().split()]
    start = inp[0]
    finish = inp[1]
    periods.append((idx, start, finish))

# periods.sort(key=lambda x: x[1], reverse=True)
# rperiods = sorted(periods, key=lambda x: x[2], reverse=True)
# index = 0
# rindex = 0
# point = periods[index][1]
# points = [point]
# while rindex < N:
#     ridx, rstart, rfinish = rperiods[rindex]
#     if rfinish < point:
#         index += 1
#         point = periods[index][1]
#         points.append(point)
#     rindex += 1

verbose = False
periods.sort(key=lambda x: x[1])
rperiods = sorted(periods, key=lambda x: x[2])
index = 0
rindex = 0
point = rperiods[rindex][2]
points = [point]
while index < len(periods):
    idx, start, finish = periods[index]
    if verbose: print("[", start, finish, "]", "point=", point)
    if start > point:
        if verbose: print("  ",start,">",point)
        _, rstart, rfinish = rperiods[rindex]
        while rstart <= point and rindex < N:
            rindex += 1
            if verbose: print("  rindex=",rindex)
            _, rstart, rfinish = rperiods[rindex]
        point = rperiods[rindex][2]
        points.append(point)
    # if verbose: print()
    index += 1

print(len(points))
print(" ".join(map(str, points)))
