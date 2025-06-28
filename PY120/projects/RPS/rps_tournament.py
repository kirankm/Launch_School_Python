import sys
import os
from time import sleep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../common")))

from tournament import Tournament
from player import HumanPlayer, R2D2, HAL, Computer, Daneel
from rps_round import RPSRound, SuddenDeathRound
from utilities import prompt

class RPSTournament(Tournament):
    def __init__(self, game, config):
        super().__init__(game)
        self._initialize_players()
        self.round_type = RPSRound

    def _initialize_players(self):
        config = self._config.options
        human_player = config['player_name']['curr_val']
        computer_player = config['computer_name']['curr_val']
        self.human = human_player
        self.computer = computer_player

    @property
    def human(self):
        return self._human

    @human.setter
    def human(self, value):
        self._human = HumanPlayer(value)

    @property
    def computer(self):
        return self._computer

    @computer.setter
    def computer(self, value):
        match value.upper():
            case "R2D2":
                self._computer = R2D2()
            case "HAL":
                self._computer = HAL()
            case "DANEEL":
                self._computer = Daneel(self)
            case _:
                self._computer = Computer(value)

    @property
    def required_wins(self):
        config = self._config.options
        try:
            return config['wins_required']['curr_val']
        except:
            return super().required_wins
        
    @property
    def sudden_death_status(self):
        config = self._config.options
        try:
            return config['sudden_death']['curr_val']
        except:
            return False

    def _display_current_settings(self):
        super()._display_current_settings()
        prompt(f"The number of wins required to win the tournament is {self.required_wins}")
        sudden_death_status = "on" if self.sudden_death_status else "off"
        prompt(f"The sudden death tie breakeris currently {sudden_death_status}")

    def _handle_tie(self):
        prompt("The current tournament is a Tie", prefix_space= True)
        if self.sudden_death_status:
            prompt("Starting the Sudden Death Round")
            sleep(2)
            self._start_sudden_death()
    
    def _start_sudden_death(self):
        new_round = SuddenDeathRound(self)
        new_round.introduce(self._game.name)
        self._rounds.append(new_round)
        new_round.play()
