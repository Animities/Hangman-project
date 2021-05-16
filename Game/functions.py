import random


def getLineCount():  # Used to allow users to add words to the list
    file = open("WordList.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1.
    line_count = int(line_count)
    file.close()
    return line_count


def findWord(List):  # Used to get the word for the game.
    randInt = random.randrange(0, len(List)) - 1
    foundWord = List[randInt]
    return foundWord