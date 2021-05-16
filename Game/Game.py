import functions


wordList = []

file = open("WordList.txt", "r")

# Fucking getting the list populated with popular words.
for i in range(functions.getLineCount()):
    appendWord = file.readline()
    appendWord = appendWord.replace("\n", "")
    if len(appendWord) > 1:
        wordList.append(appendWord)
    # print(appendWord)  # For testing purposes only.
# print(wordList)  # For testing purposes only.
file.close()


# Get random word from list


pickedWord = functions.findWord(wordList).upper()


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


def game(word):  # The main game
    guessedWord = []
    wordBin = []
    correct = False
    for x in range(len(word)):
        guessedWord.append("-")
    attemptsLeft = 12
    print(guessedWord)
    while attemptsLeft > 0:
        guesses = input("Guess a character! ").upper()
        string = ""
        if len(guesses) == 1:  # Guess a letter

            if singleCharGuess(word, guesses, wordBin, guessedWord) == 2:
                attemptsLeft -=1

            print(guessedWord)
            print("The wrong letters:", wordBin)

        elif len(guesses) > 1:  # Guess a word
            if wordGuess(guesses, word) == 1:
                score = attemptsLeft*100
                return score
            elif wordGuess(guesses, word) == 2:
                attemptsLeft -=1

        for letters in guessedWord:  # Seeing if they guessed the word without inputting a word
            string = string + letters
        if string.upper() == pickedWord.upper():
            print(word + " is right! Congratulations!")
            score = attemptsLeft * 100
            return score
        print("Current score: "+str(attemptsLeft*100))
    if not correct:
        print("Sorry, you're out of guesses. The correct word is " + word)  # Losing screen
        score = 0
        return score


def highScoreFunc(scores):  # hangman high score system
    try:
        q = open("highScore.txt", "r")
        highScore = int(q.readline())
    except FileNotFoundError:
        q = open("highScore.txt", "w")
        highScore = 0
        print("First time playing? This is my first time making a game!")
    except ValueError:
        q = open("highScore.txt", "w")
        highScore = 0
        print("There has been a value error")

    if int(scores) > int(highScore):
        w = open("highScore.txt", "w")
        w.write(str(scores))
        w.close()
        print("New high score: "+ str(scores))
    elif int(highScore) == int(scores):
        print("You tied your highest score: " + str(scores))
    else:
        print("Your score: "+str(scores)+"\nHighscore: "+str(highScore))
    q.close()


highScoreFunc(game(pickedWord))