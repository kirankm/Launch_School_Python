import random

class RPS:
    def __init__(self, config = None):
        self.config = config
        self._human = HumanPlayer()
        self._computer = Computer()
        self._rounds = []
        self._winner = None
        self._result = {'human':0, 'computer':0}

    @property
    def human(self):
        return self._human
    
    @property
    def computer(self):
        return self._computer
    
    @property
    def winner(self):
        return self._winner
    
    @property
    def result(self):
        return self._result
    
    @winner.setter
    def winner(self, winning_player):
        if not isinstance(winning_player, Player):
            raise TypeError("Winner should be a Player")
        self._winner = winning_player

    def play(self):
        self._display_welcome_message()
        while True:
            new_round = self.start_new_round()
            new_round.play()
            new_round.display_summary()
            if not(self._play_again()):
                break
        self._update_result()
        self.display_summary()
        self._display_goodbye_message()

    def start_new_round(self):
        round_number = len(self._rounds) + 1
        new_round = Round(self, round_number)
        self._rounds.append(new_round)
        return new_round

    def _play_again(self):
        prompt = "Would you like to Play again? Choose yes(y) or no(n): "
        while True:
            answer = input(prompt).lower()
            if answer in ['yes' , 'y']:
                return True
            if answer in ['no', 'n']:
                return False
            prompt = "Invalid Choice. Please choose either yes(y) or no(n): "

    def _update_result(self):
        for round in self._rounds:
            if round.winner in ('human', 'computer'):
                self.result[round.winner] = self.result[round.winner] + 1
        self._winner = max(self.result, key = self.result.get)

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_game_result(self):
        print(f"{self.human} won {self.result['human']} games")
        print(f"{self.computer} won {self.result['computer']} games")
        print(f"{self.winner} won")

    def display_summary(self):
        for round in self._rounds:
            round.display_summary(full = True)
        self._display_game_result()
        
class Round:
    def __init__(self, game, number):
        self._game = game
        self._number = number
        self._winner = None
        self._human_move = None
        self._computer_move = None

    @property
    def winner(self):
        return self._winner

    def play(self):
        self._human_move = self._game.human.choose()
        self._computer_move = self._game.computer.choose()
        self._update_result()

    def _update_result(self):
        if self._human_move > self._computer_move:
            self._winner = "human"
        elif self._human_move < self._computer_move:
            self._winner = "computer"
        else:
            self._winner = "tie"

    def display_summary(self, full = False):
        if full:
            print(f"Round {self._number}")
        print(f"You chose {self._human_move}")
        print(f"Computer chose {self._computer_move}")
        if self._winner == "tie":
            print("It's a tie")
        else:
            print(f"{self._winner} won!!")

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    def __init__(self):
        self.move = None
        self._name = None

    def choose(self):
        return NotImplemented
    
    @property
    def move(self):
        return self._move
    
    @move.setter
    def move(self, new_move):
        self._move = new_move

    def __str__(self):
        return self._name

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self._name = "Kiran"

    def choose(self):
        prompt = "Please choose rock, paper, or scissors: "
        while True:
            choice = input(prompt).lower()
            if choice in self.__class__.CHOICES:
                break
            else:
                prompt = "Sorry. Incorrect Choice. Please choose one of rock, paper, or scissors: "
        self.move = Move(choice)
        return self.move

class Computer(Player):
    def __init__(self):
        super().__init__()
        self._name = "HAL 9000"

    def choose(self):
        choice = random.choice(self.__class__.CHOICES)
        self.move = Move(choice)
        return self.move

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