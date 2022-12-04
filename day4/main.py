def solve():
    overlapCount = 0
    pairs = []
    for pair in open("input.txt").read().split("\n"):
        elfs = pair.split(',')
        elfOne = elfs[0]
        elfTwo = elfs[1]
        pairs.append((elfOne.split('-'), elfTwo.split('-')))

    for pair in pairs:
        if partialOverlap(pair[0], pair[1]):
            # print(pair)
            overlapCount += 1

    # print(pairs)
    print(overlapCount)


def partialOverlap(rangeOne, rangeTwo):
    return (int(rangeTwo[0]) <= int(rangeOne[0]) <= int(rangeTwo[1])) or (
            int(rangeTwo[0]) <= int(rangeOne[1]) <= int(rangeTwo[1])) or (
                   int(rangeOne[0]) <= int(rangeTwo[0]) <= int(rangeOne[1])) or (
                   int(rangeOne[0]) <= int(rangeTwo[1]) <= int(rangeOne[1]))


def fullyContains(rangeOne, rangeTwo):
    return (int(rangeOne[0]) >= int(rangeTwo[0]) and int(rangeOne[1]) <= int(rangeTwo[1])) or (
            int(rangeOne[0]) <= int(rangeTwo[0]) and int(rangeOne[1]) >= int(rangeTwo[1]))


if __name__ == '__main__':
    solve()
