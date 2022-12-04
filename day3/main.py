from string import ascii_letters

def solve():
    scoremap = dict()
    i = 1
    for letter in ascii_letters:
        scoremap.update({letter: i})
        i += 1
    prioritySum = 0
    rucksacks = []
    for rucksack in open("input.txt").read().split("\n"):
        rucksacks.append([*rucksack])

    index = 0
    for rucksackindex in range(len(rucksacks)//3):
        bagOne = rucksacks[index]
        bagTwo = rucksacks[index + 1]
        bagThree = rucksacks[index + 2]
        print("bagOne: " + str(bagOne))
        print("bagTwo: " + str(bagTwo))
        print("bagThree: " + str(bagThree))
        intersectionOne = [value for value in bagOne if value in bagTwo]
        intersectionFinal = [value for value in bagThree if value in intersectionOne]
        intersectionFinal = list(dict.fromkeys(intersectionFinal))
        print(intersectionFinal)
        prioritySum += scoremap[intersectionFinal[0]]
        if(len(intersectionFinal) > 1) : break
        index += 3



    print(prioritySum)

if __name__ == '__main__':
    solve()

