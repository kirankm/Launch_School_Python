import shutil
from time import sleep

from utilities import clear_screen, prompt, load_json_file
from round import Round, SuddenDeathRound
from player import Player, HumanPlayer, Computer, R2D2, Daneel, HAL

class Banner:
    BANNER_WIDTH = shutil.get_terminal_size().columns
    def __init__(self, message):
        self._msg = message.upper()

    def display(self):
        line1 = "*" * Banner.BANNER_WIDTH
        line2 = f"*{' '*(Banner.BANNER_WIDTH-2)}*"
        line3 = f"*{self._msg.center(Banner.BANNER_WIDTH - 2)}*"
        banner = [line1, line2, line3, line2, line1]
        print("\n".join(banner))

class Game:
    def __init__(self, game_name = None, config = None):
        self._config = self._load_config(config)
        self._human = HumanPlayer(self._config['player_name'])
        self.computer = self._config['Computer_AI']
        self._rounds = []
        self._winner = None
        self._game_name = "Rock Paper Scissor Spock Lizard"
        self._result = {'human':0, 'computer':0}
        self._banner = Banner(self._game_name)

    def _load_config(self, config):
        if config is None:
            return None
        return load_json_file(config)

    @property
    def human(self):
        return self._human

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
    def rounds(self):
        return self._rounds
    
    @property
    def winner(self):
        return self._winner
    
    @winner.setter
    def winner(self, winning_player):
        if winning_player == "human":
            winning_player = self.human
        elif winning_player == "computer":
            winning_player = self.computer
        if not isinstance(winning_player, Player):
            raise TypeError("Winner should be a Player")
        self._winner = winning_player

    @property
    def result(self):
        return self._result

    @property
    def banner(self):
        return self._banner
    
    def play(self):
        self._display_welcome_message()
        while True:
            new_round = self.start_new_round()
            new_round.play()
            self._update_result(new_round)
            if not(self._play_again()):
                break
        self._declare_winner()
        self._display_goodbye_message()

    def _display_welcome_message(self):
        clear_screen(self._banner)
        msg = f"Let's start a new game of {self._game_name}!"
        prompt(msg, prefix_space= True)

    def start_new_round(self):
        round_number = len(self._rounds) + 1
        new_round = Round(self, round_number)
        new_round.display_welcome_message(self.banner)
        self._display_current_score()
        self._rounds.append(new_round)
        return new_round

    def _display_current_score(self):
        if not self._rounds:
            summary = f"Current Score: {self._human} 0, {self._computer}:0"
        else:
            leader, lagger = self._get_leader_lagger()
            lead_player = self.human if leader == 'human' else self.computer
            lag_player = self.human if lagger == 'human' else self.computer
            if leader:
                summary = "".join([
                    f"{lead_player} leads {lag_player} by ",
                    f"{self._get_lead()} after {self._get_game_count()}."
                ])
            else:
                summary = "".join([
                    f"After {self._get_game_count()} the game is tied with ",
                    f"each player winning {self._result['human']} games."
                ]).capitalize()
        prompt(summary)

    def _get_leader_lagger(self):
        if self._result['human'] == self._result['computer']:
            return None, None
        return sorted(self._result, key = self._result.get, reverse= True)

    def _get_lead(self):
        lead = abs(self._result['human'] - self._result['computer'])
        suffix = 's' if lead > 1 else ''
        return f"{lead} point{suffix}"
    
    def _get_game_count(self):
        games_played = len(self._rounds)
        suffix = 's' if games_played > 1 else ''
        return f"{games_played} game{suffix}"

    def _update_result(self, round):
        winner_type = None if round.winner is None else round.winner.type
        if winner_type in ('human', 'computer'):
            self.result[winner_type] = self.result[winner_type] + 1

    def _play_again(self):
        msg = "Would you like to Play again? Choose yes(y) or no(n): "
        while True:
            prompt(msg, prefix_space = True)
            answer = input().lower()
            if answer in ['yes' , 'y']:
                return True
            if answer in ['no', 'n']:
                return False
            msg = "Invalid Choice. Please choose either yes(y) or no(n): "    
        
    def _declare_winner(self):
        prompt("Final Results", prefix_space= True)
        prompt(f"{self.human}: Score {self._result['human']}", 
                                            prefix_space= True)
        prompt(f"{self.computer}: Score {self._result['computer']}")

        if self.result['human'] > self.result['computer']:
            prompt(f"{self.human} has won the tournament", prefix_space= True)
        elif self.result['human'] < self.result['computer']:
            prompt(f"{self.computer} has won the tournament", prefix_space= True)
        else:
            prompt("The current tournament is a Tie", prefix_space= True)
            prompt("Starting the Sudden Death Round")
            sleep(2)
            self._start_sudden_death()

    def _start_sudden_death(self):
        new_round = SuddenDeathRound(self)
        new_round.display_welcome_message(self.banner)
        self._rounds.append(new_round)
        new_round.play()

    def _display_goodbye_message(self):
        msg = f"Thanks for playing {self._game_name}. Goodbye!"
        prompt(msg, prefix_space= True)

    def display_summary(self):
        for round in self._rounds:
            round._display_result(full = True)
        self._display_result()

    def _display_result(self):
        total_games = len(self._rounds)
        computer_wins = self.result['computer']
        human_wins = self.result['human']
        prompt(f"{self.human} won {human_wins} games")
        prompt(f"{self.computer} won {computer_wins} games")
        if total_games > human_wins + computer_wins:
            prompt(f"{total_games - (human_wins + computer_wins)} games were tied.")

game_name = "Rock Paper Scissor Lizard Spock"            
config_path = "rps_config.json"
Game(game_name, config_path).play()