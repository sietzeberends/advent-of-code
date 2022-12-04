def solve():
    highestTotal = 0
    secondHighest = 0
    thirdHighest = 0
    for elf in open("input.txt").read().split("\n\n"):
        elfTotal = 0
        for fooditem in elf.split("\n"):
            elfTotal += int(fooditem)
        if elfTotal > highestTotal:
            thirdHighest = secondHighest
            secondHighest = highestTotal
            highestTotal = elfTotal

    print(highestTotal)
    print(highestTotal + secondHighest + thirdHighest)

if __name__ == '__main__':
    solve()
