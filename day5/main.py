from collections import deque

def solve():
    replacements = []
    stacks = []

    with open("input.txt") as file:
        rows = file.readlines()[10:]
        rowCount = 0
        for row in rows:
            replacements.append({})
            if (row[6].isdigit()) :
                noOfCrates = row[5:7]
            else:
                noOfCrates = row[5]
            if (row[6].isdigit()):
                start = row[13:14]
            else:
                start = row[12]
            if row[6].isdigit():
                end = row[18:19]
            else:
                end = row[17]
            replacements[rowCount] = {"noOfCrates": int(noOfCrates), "start": int(start) - 1, "end": int(end) - 1}
            rowCount += 1
        print (replacements)
    with open("input.txt") as file:
        rows = file.readlines()[0:8]
        file.seek(0)
        numbers = file.readlines()[8].replace(" ", "").strip("\n")
        for number in numbers:
            stacks.append(deque())
        counter = 0
        for row in rows:
            for chars in range(0, len(row) // 4):
                char = row[counter * 4:chars * 4 + 3]
                if char != '   ':
                    stacks[counter].append(char)
                counter += 1
            counter = 0
    for stack in stacks:
        print(stack)
    print("------------------------------------------------------------------")

    for replacement in replacements:
        start = replacement["start"]
        end = replacement["end"]
        stackFrom = deque(stacks[start])
        stackTo = deque(stacks[end])
        noOfCrates = replacement.get("noOfCrates")
        if (noOfCrates > 1) :
            cratesPreMove = deque()
            for crateToMove in range(1, replacement.get("noOfCrates") + 1):
                if len(stackFrom) != 0:
                    cratesPreMove.append(stackFrom.popleft())
            for crateToMove in range(1, replacement.get("noOfCrates") + 1):
                if len(cratesPreMove) != 0:
                    stackTo.appendleft(cratesPreMove.pop())
                    stacks[start] = stackFrom
                    stacks[end] = stackTo
        else:
            for crateToMove in range(1, replacement.get("noOfCrates") + 1):
                if len(stackFrom) != 0:
                    stackTo.appendleft(stackFrom.popleft())
                    stacks[start] = stackFrom
                    stacks[end] = stackTo
    for stack in stacks:
        print(stack)

if __name__ == '__main__':
    solve()
