import random


class Hangman:
    def __init__(self, word):
        self.word = word
        self.letters_guessed = []
        self.errors_made = 0
        self.max_errors = 6

    def guess_letter(self, letter):
        if not letter or not letter in self.word:
            self.errors_made += 1

        self.letters_guessed.append(letter)

    def get_word_progress(self):
        progress = ""

        for letter in self.word:
            if letter in self.letters_guessed:
                progress += letter
            else:
                progress += "_"

        return progress

    def get_tries_left(self):
        return self.max_errors - self.errors_made

    def has_won(self):
        if not "_" in self.get_word_progress():
            return True

        return False

    def has_lost(self):
        if self.get_tries_left() == 0:
            return True

        return False


def play_hangman():

    print("Welcome to Hangman 2!!!\n")

    # Choose a random word
    words = ["apple", "banana", "orange", "strawberry"]
    word = random.choice(words)

    # Create a Hangman game with the chosen word
    game = Hangman(word)

    # Game loop
    while not game.has_won() and not game.has_lost():
        progress = game.get_word_progress()
        print(f"\nTries: {game.get_tries_left()}")
        print(f"Word progress: {progress}")
        letter = input("Guess a letter: ")
        game.guess_letter(letter)

    print("")

    if game.has_won():
        print("You won!")
    else:
        print("You lost :(")


# Start the game
play_hangman()
