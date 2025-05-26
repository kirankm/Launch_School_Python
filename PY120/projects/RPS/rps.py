import random

class RPS:
    def __init__(self, config = None):
        self.config = config
        self._human = HumanPlayer()
        self._computer = Computer()
        self._score = {}

    def play(self):
        self._display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not(self._play_again()):
                break
        self._display_goodbye_message()

    def _play_again(self):
        prompt = "Would you like to Play again? Choose yes(y) or no(n): "
        while True:
            answer = input(prompt).lower()
            if answer in ['yes' , 'y']:
                return True
            if answer in ['no', 'n']:
                return False
            prompt = "Invalid Choice. Please choose either yes(y) or no(n): "
    
    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        print(f"You chose {self._human.move}")
        print(f"Computer chose {self._computer.move}")
        if self._human.move > self._computer.move:
            print("You Win!!")
        elif self._human.move < self._computer.move:
            print("Computer Wins")
        else:
            print("It's a tie!!")
        
class Round:
    def __init__(self, human, computer):
        self._human = human
        self._computer = computer
        self.winner = None
        

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    def __init__(self):
        self.move = None

    def choose(self):
        return NotImplemented
    
    @property
    def move(self):
        return self._move
    
    @move.setter
    def move(self, new_move):
        self._move = new_move

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = "Please choose rock, paper, or scissors: "
        while True:
            choice = input(prompt).lower()
            if choice in self.__class__.CHOICES:
                break
            else:
                prompt = "Sorry. Incorrect Choice. Please choose one of rock, paper, or scissors: "
        self.move = Move(choice)

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = random.choice(self.__class__.CHOICES)
        self.move = Move(choice)

class Move:
    MOVE_RULES = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __gt__(self, other):
        if isinstance(other, Move):
            return self.__class__.MOVE_RULES[self.value] == other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Move):
            return self.__class__.MOVE_RULES[other.value] == self.value
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Move):
            return other.value == self.value
        return NotImplemented

    def __str__(self):
        return self.value

RPS().play()