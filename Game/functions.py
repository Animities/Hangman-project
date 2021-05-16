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


def singleCharGuess(pWord, UiGuess, wBin, gWord):
    if pWord.find(UiGuess) != -1:
        for j in range(len(pickedWord)):
            if pickedWord[j].upper() == UiGuess.upper():
                gWord[j] = UiGuess.upper()
                return 0

    elif UiGuess in wBin:
        print("You've already guessed this letter.")
        return 1

    else:
        wBin.append(UiGuess)
        wBin.sort()
        return 2


def wordGuess(UiGuess, pWord):
    if UiGuess.upper() == pWord.upper():
        print(pWord + " is right! Congratulations!")
        return 1
    else:
        print("Sorry, that's not the word!")
        return 2