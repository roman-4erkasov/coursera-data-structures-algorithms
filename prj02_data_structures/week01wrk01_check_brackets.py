# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    closing_set = {("(",")"),("[","]"),("{","}")}
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            # pass
            opening_brackets_stack.append((next, i))
        if next in ")]}":
            # Process closing bracket, write your code here
            # pass
            if opening_brackets_stack:
                top, idx = opening_brackets_stack[-1]
                if (top, next) in closing_set:
                    del opening_brackets_stack[-1]
                else:
                    return i+1
            else:
                return i+1

    if opening_brackets_stack:
        return opening_brackets_stack[-1][1]+1
    else:
        return None


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch is None:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
