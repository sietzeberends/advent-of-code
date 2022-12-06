from collections import deque

def solve():
    chars = open("input.txt").read()
    startIndex = 0
    for endIndex in range(0 , len(chars)):
        fourChars = chars[startIndex:endIndex + 14]
        if len(fourChars) == len(set(fourChars)):
            print(endIndex+5)
            print(fourChars)
        startIndex += 1


if __name__ == '__main__':
    solve()
