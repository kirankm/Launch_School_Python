from time import sleep
from utilities import clear_screen, prompt, get_user_input

class Tournament:
    def __init__(self, game):
        self._game = game
        self._rounds = []
        self._config = self._game.config_menu
        self._result = {'human' : 0, 'computer' : 0}
        self._human = None
        self._computer = None
        self._round_type = None

    @property
    def winner(self):
        if max(self._result.values()) < self.required_wins:
            return None
        elif self._result['human'] == self.required_wins:
            return self._human
        return self._computer

    @property
    def required_wins(self):
        return float('inf')
    
    @property
    def round_type(self):
        return self._round_type

    @round_type.setter
    def round_type(self, round_type):
        self._round_type = round_type

    def play(self):
        self._introduce()
        while not(self.winner):
            new_round = self._start_new_round()
            new_round.play()
            self._update_result(new_round)
            if not self._play_again():
                break
        self._end_tournament()
        sleep(2)
        self._game.main_menu.display()

    def _introduce(self):
        clear_screen(self._game.name)
        msg = f"Let's start a new tournament of {self._game.name}!"
        prompt(msg, prefix_space= True)
        self._display_current_settings()

    def _start_new_round(self):
        round_number = len(self._rounds) + 1
        new_round = self._round_type(self, round_number)
        new_round.introduce(self._game.name)
        self._display_current_score()
        self._rounds.append(new_round)
        return new_round
    
    def _update_result(self, rnd):
        winner_type = None if rnd.winner is None else rnd.winner.player_type
        if winner_type in ('human', 'computer'):
            self._result[winner_type] = self._result[winner_type] + 1

    def _play_again(self):
        intro_msg = "Would you like to Play again? Choose yes(y) or no(n): "
        error_msg = "Invalid Choice. Please choose either yes(y) or no(n): "
        choices = ['y', 'yes', 'no', 'n']
        user_choice = get_user_input(intro_msg, error_msg, choices)
        return user_choice[0] == "y"

    def _end_tournament(self):
        self._display_final_scores()
        if self._result['human'] > self._result['computer']:
            self._display_winner(self._human)
        elif self._result['human'] < self._result['computer']:
            self._display_winner(self._computer)
        else:
            self._handle_tie()
        self._display_goodbye_message()
    
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

    def _display_current_settings(self):
        prompt(f"Human Player is {self.human}", prefix_space= True)
        prompt(f"Computer Player is {self.computer}")
    
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

    def _display_final_scores(self):
        prompt("Final Scores:", prefix_space=True)
        prompt(f"{self._human}: {self._result['human']}")
        prompt(f"{self._computer}: {self._result['computer']}")
    
    def _display_winner(self, winner):
        prompt(f"{winner} wins the tournament!", prefix_space=True)
    
    def _handle_tie(self):
        return NotImplemented
    
    def _display_goodbye_message(self):
        msg = f"Thanks for playing {self._game.name}. Goodbye!"
        prompt(msg, prefix_space= True)




