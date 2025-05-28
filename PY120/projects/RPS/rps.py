import random
import pdb
import shutil
from utilities import clear_screen, prompt

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

class RPS:
    def __init__(self, config = None):
        self.config = config
        self._human = HumanPlayer()
        self._computer = Computer()
        self._rounds = []
        self._winner = None
        self._result = {'human':0, 'computer':0}
        self._banner = Banner("Rock Paper Scissor Spock Lizard")

    @property
    def human(self):
        return self._human
    
    @property
    def computer(self):
        return self._computer
    
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
            self._display_current_score()
            new_round = self.start_new_round()
            new_round.play()
            self._update_result(new_round)
            if not(self._play_again()):
                break
        #self.display_summary()
        self._declare_winner()
        self._display_goodbye_message()

    def start_new_round(self):
        round_number = len(self._rounds) + 1
        new_round = Round(self, round_number)
        new_round.display_welcome_message(self.banner)
        self._display_current_score()
        self._rounds.append(new_round)
        return new_round

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

    def _update_result(self, round):
        if round.winner in ('human', 'computer'):
            self.result[round.winner] = self.result[round.winner] + 1

    def _display_welcome_message(self):
        clear_screen(self._banner)
        msg = "Let's start a new game of Rock Paper Scissors Lizard Spock!"
        prompt(msg, prefix_space= True)

    def _display_goodbye_message(self):
        msg = "Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!"
        prompt(msg, prefix_space= True)

    def _display_current_score(self):
        pass

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

    def _display_result(self):
        total_games = len(self._rounds)
        computer_wins = self.result['computer']
        human_wins = self.result['human']
        prompt(f"{self.human} won {human_wins} games")
        prompt(f"{self.computer} won {computer_wins} games")
        if total_games > human_wins + computer_wins:
            prompt(f"{total_games - (human_wins + computer_wins)} games were tied. ")
        
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
            self._start_sudden_death()

    def _start_sudden_death(self):
        pass

    def display_summary(self):
        for round in self._rounds:
            round._display_result(full = True)
        self._display_result()

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
    
    @winner.setter
    def winner(self, winning_player):
        self._winner = winning_player

    def display_welcome_message(self, banner):
        if self._number > 1:
            clear_screen(banner)
        prompt(f"Let's Start ROUND {self._number}", prefix_space = True)

    def play(self):
        while self.winner is None:
            self._human_move = self._game.human.choose()
            self._computer_move = self._game.computer.choose()
            self._update_result()
            self._display_result()
            if (self.winner is None) and not(self._repeat_round()):
                break

    def _repeat_round(self):
        msg = "Last round was a Tie. Would you like to Repeat it? Choose yes(y) or no(n): "
        while True:
            prompt(msg, prefix_space = True)
            answer = input().lower()
            if answer in ['yes' , 'y']:
                return True
            if answer in ['no', 'n']:
                return False
            msg = "Invalid Choice. Please choose either yes(y) or no(n): "

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
        elif self.winner == "human":
            self._declare_victory('human')
        elif self.winner == "computer":
            self._declare_victory('computer')
    
    def _declare_victory(self, winner):
        winning_move, losing_move, winning_player = (
            (self._human_move,    self._computer_move, self._game.human)
            if winner == "human"
            else (self._computer_move, self._human_move, self._game.computer)
        )
        action = winning_move.get_verb(losing_move)
        prompt(f"{winning_move} {action} {losing_move}", prefix_space= True)
        prompt(f"{winning_player} wins the round")
    
class Player:
    CHOICES = {
        "R": "ROCK",
        "P": "PAPER",
        "S": "SCISSORS",
        "L": "LIZARD",
        "SP": "SPOCK"
    }

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

    def _get_choose_msg(self):
        choices = self.__class__.CHOICES
        msg = "Please choose one of the following\n" + \
            "\n".join([f"{k.lower()} for {v}" for k,v in choices.items()])
        return msg
    
    def choose(self):
        msg = self._get_choose_msg()
        while True:
            prompt(msg, prefix_space= True)
            choice = input().upper()
            if choice in self.__class__.CHOICES:
                choice = self.__class__.CHOICES[choice]
                break
            elif choice in self.__class__.CHOICES.values():
                break
            else:
                msg = "Sorry. Incorrect Choice. Please choose one of rock, paper, scissors, lizard or spock: "
        self.move = Move(choice)
        return self.move

class Computer(Player):
    def __init__(self):
        super().__init__()
        self._name = "HAL 9000"

    def choose(self):
        options = list(self.__class__.CHOICES.values())
        choice = random.choice(options)
        self.move = Move(choice)
        return self.move

class Move:
    MOVE_RULES = {
        "SCISSORS": {
        "PAPER": "CUTS",
        "LIZARD": "DECAPITATES"
        },
        "PAPER": {
        "ROCK": "COVERS",
        "SPOCK": "DISPROVES"
        },
        "ROCK": {
        "LIZARD": "CRUSHES",
        "SCISSORS": "CRUSHES"
        },
        "LIZARD": {
        "SPOCK": "POISONS",
        "PAPER": "EATS"
        },
        "SPOCK": {
        "SCISSORS": "SMASHES",
        "ROCK": "VAPORIZES"
        }
    }

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __gt__(self, other):
        if isinstance(other, Move):
            return other.value in self.__class__.MOVE_RULES[self.value] 
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Move):
            return self.value in self.__class__.MOVE_RULES[other.value]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Move):
            return other.value == self.value
        return NotImplemented

    def __str__(self):
        return self.value
    
    def get_verb(self, other):
        return self.__class__.MOVE_RULES[self.value][other.value]

RPS().play()