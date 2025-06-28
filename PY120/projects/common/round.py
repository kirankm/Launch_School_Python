from utilities import clear_screen, prompt

class Round:
    def __init__(self, game, number):
        self._game = game
        self._number = number
        self._winner = None

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winning_player):
        if winning_player == "human":
            self._winner = self._game.human
        elif winning_player == "computer":
            self._winner = self._game.computer
    
    def introduce(self, game_name):
        if self._number != 1:
            clear_screen(game_name)
        prompt(f"Let's Start ROUND {self._number}", prefix_space = True)

    def play(self):
        return NotImplemented
    
    def _update_result(self):
        return NotImplemented
    
    def _display_result(self):
        if self.winner:
            self._declare_victory(self.winner.player_type)
        else:
            prompt("It's a tie", prefix_space= True)

    def _declare_victory(self, winner):
        prompt(f"{self.winner} wins ROUND {self._number}")

