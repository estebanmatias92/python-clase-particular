import random


class JuegoAhorcado:
    def __init__(self, words):
        self.__words = words
        # Welcome the player
        print("Welcome to Hangman!!!\n")

    def _initialize_values(self):
        self.__word = random.choice(self.__words)
        self.__letters_to_guess = set(self.__word)
        self.__guessed_letters = set()
        self.__tries = 7

    def _print_main_screen(self):
        # Show the player their progress
        print("\nYou have {} tries {}.".format(self.__tries, "left"))
        # print("Used letters: {}".format(" ".join(self.__guessed_letters)))
        print("Word: {}".format(self._get_clues()))

    def _print_win_message(self):
        print("\nCongratulations! You won!")

    def _print_lose_message(self):
        print("\nSorry, you lost. The word was {}.".format(self.__word))

    def _get_clues(self):
        # Return the word with unguessed letters replaced by underscores
        return "".join(
            letter if letter in self.__guessed_letters else "_"
            for letter in self.__word
        )

    def _is_won(self):
        return not self.__letters_to_guess

    def _is_lost(self):
        return self.__tries <= 0

    def start(self):
        # Initialize the game with default values
        self._initialize_values()

        # Set up the game loop
        while not self._is_won() and not self._is_lost():

            self._print_main_screen()

            # Get a letter from the player
            letter = input("Enter a letter: ").lower()

            # Check if the letter is in the word
            if letter in self.__letters_to_guess:
                self.__guessed_letters.add(letter)
                self.__letters_to_guess.remove(letter)
            else:
                self.__tries -= 1

            # Check if the player has won
            if self._is_won():
                self._print_win_message()

        if self._is_lost():
            self._print_lose_message()


def play_hangman():
    palabras = ["banana", "frutilla", "melon", "sandia"]
    juego = JuegoAhorcado(palabras)

    juego.start()


# Start the game
play_hangman()
