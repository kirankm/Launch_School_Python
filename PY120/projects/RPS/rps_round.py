from utilities import prompt
from round import Round


class RPSRound(Round):
    def __init__(self, game, number):
        super().__init__(game, number)
        self._human_move = None
        self._computer_move = None

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

    def _display_result(self):
        prompt(f"{self._game.human} chose {self._human_move}",
                                            prefix_space= True)
        prompt(f"{self._game.computer} chose {self._computer_move}")
        super()._display_result()

    def _declare_victory(self, winner):
        winning_move, losing_move = (
            (self._human_move,    self._computer_move)
            if winner == "human"
            else (self._computer_move, self._human_move)
        )
        action = winning_move.get_verb(losing_move)
        prompt(f"{winning_move} {action} {losing_move}", prefix_space= True)
        super()._declare_victory(winner)

class SuddenDeathRound(RPSRound):
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
