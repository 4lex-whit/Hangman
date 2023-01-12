import random

STAGES = ["""┌──┐
│
│
│
└────""","""┌──┐
│  o
│
│
└────""","""┌──┐
│  o
│  |
│
└────""","""┌──┐
│  o
│ /|
│
└────""","""┌──┐
│  o
│ /|\\
│
└────""","""┌──┐
│  o
│ /|\\
│ /
└────""","""┌──┐
│  o
│ /|\\
│ / \\
└────"""]

class Hangman():
    def __init__(self):
        self.__word = None
        self.__correctGuesses = []
        self.__incorrectGuesses = []
    
    def getWord(self):
        return self.__word
    def setNewWord(self):
        wordsLines = open("words.txt", "r").readlines()
        self.__word = wordsLines[random.randint(0, len(wordsLines) - 1)].replace("\n", "")

    def getCorrectGuesses(self):
        return self.__correctGuesses
    def getIncorrectGuesses(self):
        return self.__incorrectGuesses

    def getHiddenWord(self):
        hiddenWord = ""
        letters = list(self.getWord())
        for i in range(len(letters)):
            if letters[i] in self.getCorrectGuesses():
                hiddenWord += letters[i]
            else:
                hiddenWord += "╳"
        return hiddenWord

    def getGuess(self):
        guess = input("> ")
        if guess.isalpha() != True:
            print("You can only guess letters")
            return self.getGuess()
        if len(list(guess)) != 1:
            print("You can only guess one letter")
            return self.getGuess()
        if guess in self.getCorrectGuesses() or guess in self.getIncorrectGuesses():
            print("You have already guessed this letter")
            return self.getGuess()
        return guess

    def isGameOver(self):
        if len(self.getIncorrectGuesses()) == 7:
            return True
        for i in range(len(list(self.getWord()))):
            if list(self.getWord())[i] not in self.getCorrectGuesses():
                return False
        return True

    def checkGuess(self, guess):
        if guess in list(self.getWord()):
            self.getCorrectGuesses().append(guess)
        else:
            self.getIncorrectGuesses().append(guess)
    
    def main(self):
        print("┌──────────────────────────┐\n│ Hangman By Alex Whitaker │\n└──────────────────────────┘\n")
        self.setNewWord()

        while self.isGameOver() != True:
            print(self.getHiddenWord())
            self.checkGuess(self.getGuess())
            print()

            if len(self.getIncorrectGuesses()) != 0:
                print(f"{STAGES[len(self.getIncorrectGuesses()) - 1]}")

        print("Game Over")
        print(f"The word was: {self.getWord()}")

        print("\nWould you like to play again? (y/n)")
        if input("> ") == "y":
            print("\n")
            hangman = Hangman()
            hangman.main()

hangman = Hangman()
hangman.main()
