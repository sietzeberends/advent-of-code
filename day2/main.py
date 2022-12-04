# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solve():
    score = 0
    for round in open("input.txt").read().split("\n"):
        opponentChoice = getChoice(round[0])
        myChoice = getMyChoice(opponentChoice, round[2])
        score += choicePoints(myChoice)
        score += winnerPoints(opponentChoice, myChoice)
    print(score)



def getChoice(letter) :
    if letter == "A":
        return "ROCK"
    if letter == "B":
        return "PAPER"
    if letter == "C":
        return "SCISSORS"

    if letter == "X":
        return "ROCK"
    if letter == "Y":
        return "PAPER"
    if letter == "Z":
        return "SCISSORS"

#  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
def getMyChoice(opponentChoice, strategy):
    if opponentChoice == "ROCK":
        if strategy == "X":
            return "SCISSORS"
        if strategy == "Y":
            return "ROCK"
        if strategy == "Z":
            return "PAPER"
    if opponentChoice == "PAPER":
        if strategy == "X":
            return "ROCK"
        if strategy == "Y":
            return "PAPER"
        if strategy == "Z":
            return "SCISSORS"
    if opponentChoice == "SCISSORS":
        if strategy == "X":
            return "PAPER"
        if strategy == "Y":
            return "SCISSORS"
        if strategy == "Z":
            return "ROCK"
def winnerPoints(opponentChoice, myChoice):
    if myChoice == "ROCK":
        if opponentChoice == "ROCK":
            return 3
        if opponentChoice == "PAPER":
            return 0
        if opponentChoice == "SCISSORS":
            return 6

    if myChoice == "PAPER":
        if opponentChoice == "ROCK":
            return 6
        if opponentChoice == "PAPER":
            return 3
        if opponentChoice == "SCISSORS":
            return 0
    if myChoice == "SCISSORS":
        if opponentChoice == "ROCK":
            return 0
        if opponentChoice == "PAPER":
            return 6
        if opponentChoice == "SCISSORS":
            return 3


def choicePoints(myChoice):
    if myChoice == "ROCK":
        return 1
    if myChoice == "PAPER":
        return 2
    if myChoice == "SCISSORS":
        return 3

if __name__ == '__main__':
    solve()

