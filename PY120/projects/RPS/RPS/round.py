from utilities import clear_screen, prompt
from player import Player

class Round:
    def __init__(self, game, number):
        self._game = game
        self._number = number
        self._winner = None
        self._human_move = None
        self._computer_move = None

    @property
    def human_move(self):
        return self._human_move
    
    @property
    def winner(self):
        return self._winner
    
    @winner.setter
    def winner(self, winning_player):
        if winning_player == "human":
            winning_player = self._game.human
        elif winning_player == "computer":
            winning_player = self._game.computer
        if not isinstance(winning_player, Player):
            raise TypeError("Winner should be a Player")
        self._winner = winning_player

    def display_welcome_message(self, banner):
        if self._number != 1:
            clear_screen(banner)
        prompt(f"Let's Start ROUND {self._number}", prefix_space = True)

    def play(self):
        self._human_move = self._game.human.choose()
        self._computer_move = self._game.computer.choose()
        self._update_result()
        self._display_result()

    def _update_result(self):
        if self._human_move > self._computer_move:
            self.winner = "human"
        elif self._human_move < self._computer_move:
            self.winner = "computer"

    def _display_result(self, full = False):
        if full:
            prompt(f"Round {self._number}")
        prompt(f"{self._game.human} chose {self._human_move}", 
                                            prefix_space= True)
        prompt(f"{self._game.computer} chose {self._computer_move}")
        if self._winner is None:
            prompt("It's a tie", prefix_space= True)
        elif self.winner == self._game.human:
            self._declare_victory('human')
        elif self.winner == self._game.computer:
            self._declare_victory('computer')
    
    def _declare_victory(self, winner):
        winning_move, losing_move = (
            (self._human_move,    self._computer_move)
            if winner == "human"
            else (self._computer_move, self._human_move)
        )
        action = winning_move.get_verb(losing_move)
        prompt(f"{winning_move} {action} {losing_move}", prefix_space= True)
        prompt(f"{self.winner} wins the round")

class SuddenDeathRound(Round):
    def __init__(self, game):
        super().__init__(game, "SUDDEN DEATH")

    def display_welcome_message(self, banner):
        super().display_welcome_message(banner)
        prompt("Round will continue till we have a winner")

    def play(self):
        while self.winner is None:
            self._human_move = self._game.human.choose()
            self._computer_move = self._game.computer.choose()
            self._update_result()
            self._display_result()
            if self.winner is None:
                prompt("Playing Again till we have a winner")
        prompt(f"{self.winner} wins the tournament by winning the Sudden Death")

    