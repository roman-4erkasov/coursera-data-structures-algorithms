# Uses python3
"""
You are given a primitive calculator that can perform the following three operations
with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal
is given a positive integer 𝑛, find the minimum number of operations needed to obtain
the number 𝑛 starting from the number 1.

Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 106.
Output Format. In the first line, output the minimum number 𝑘 of operations needed to get 𝑛
from 1. In the second line output a sequence of intermediate numbers. That is, the second
line should contain positiveintegers 𝑎0,𝑎2,...,𝑎𝑘−1 suchthat𝑎0 =1,𝑎𝑘−1 =𝑛andforall0≤𝑖<𝑘−1,𝑎𝑖+1
isequalto either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. If there are many such sequences, output any one of them.


Sample 1.
Input:
1
Output:
0
1


Sample 2.
Input:
5
Output:
3
1 2 4 5
Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3 and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.


Sample 3.
Input:
96234
Output:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234

Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234”.
"""


def operation_inc(number, opcode):
    if opcode == 1:
        return number * 3
    elif opcode == 2:
        return number * 2
    elif opcode == 3:
        return number + 1


def operation_dec(number, opcode, verbose=None):
    result = None
    if opcode == 1:
        result = number / 3
    elif opcode == 2:
        result = number / 2
    elif opcode == 3:
        result = number - 1
    else:
        raise Exception()
    if verbose:
        print("operation_dec:", number, opcode,result)
    if float.is_integer(float(result)):
        return int(result)
    else:
        return None


def forward(number, verbose=None):
    track_min = {
        1: 0
    }
    history = []
    for num in range(2, number + 1):
        opt_choice = track_min[num - 1] + 1
        opt_op = 3
        for op in range(1, 3):
            backstep = operation_dec(num, op, verbose)
            if backstep is not None:
                curr = track_min[backstep]+1
                if curr < opt_choice:
                    opt_choice = curr
                    opt_op= op
                if verbose:
                    print("forward: op=",op,"curr=",curr)
        track_min[num] = opt_choice
        if verbose:
            print("forward:", track_min)
        history.append(opt_op)
    return track_min[number], history


def backward(history, number):
    result = []
    history_ext=[0,3]+history
    num = number
    while num >= 1:
        op = history_ext[num]
        result.append(num)
        num = operation_dec(num, op)
    return list(reversed(result))


if __name__ == '__main__':
    x= int(input())#96234
    num,hist = forward(x)
    res = backward(hist, x)
    print(num)
    print(" ".join([str(i) for i in res]))

