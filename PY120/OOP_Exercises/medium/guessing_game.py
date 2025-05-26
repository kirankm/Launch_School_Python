from random import randint
import math

class GuessingGame:
    def __init__(self, low = 1, high = 100):
        self.low = low
        self.high = high
        self.number_of_guesses = int(math.log2(high - low + 1)) + 1
        self.is_winner = False

    def get_user_guess(self):
        user_guess = int(input(f"Enter a number between {self.low} and {self.high}: "))
        while not(self.low <= user_guess <= self.high):
            user_guess = int(input(f"Invalid guess. Enter a number between {self.low} and {self.high}: "))
        return user_guess

    def play(self):
        self.reset_game()
        while not(self.is_winner) and (self.remaining_guess):
            self.play_round()
        self.display_result()
    
    def reset_game(self):
        self.number = randint(self.low, self.high)
        self.remaining_guess = self.number_of_guesses
        self.is_winner = False
        print("\n")

    def play_round(self):
        print(f"You have {self.remaining_guess} guesses remaining")
        guess = self.get_user_guess()
        self.remaining_guess -= 1
        self.display_guess_status(guess)
        if guess == self.number:
            self.is_winner = True


    def display_guess_status(self, guess):
        if guess < self.number:
            print("Your guess is too low.")
        elif guess == self.number:
            print("That's the number!")
        else:
            print("Your guess is too high.")
        print("\n")

    def display_result(self):
        if self.is_winner:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")

game = GuessingGame(501, 1500)
game.play()
