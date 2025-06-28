import random
from utilities import prompt

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
        self.player_type = None

    def choose(self):
        return NotImplemented

    @property
    def move(self):
        return self._move

    @move.setter
    def move(self, new_move):
        self._move = new_move

    @property
    def player_type(self):
        return self._player_type.lower()

    @player_type.setter
    def player_type(self, player_type):
        self._player_type = player_type

    def __str__(self):
        return str(self._name)

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.player_type = 'human'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            name = str(name)
        if len(name.strip()) == 0:
            raise ValueError("Empty strings not alowed for name")
        self._name = name

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
            if choice in self.__class__.CHOICES.values():
                break
            msg = "Sorry. Incorrect Choice. Please choose one of rock(r), paper(p), scissors(s), lizard(l) or spock(sp): "
        self.move = Move(choice)
        return self.move

class Computer(Player):
    def __init__(self, name = "Computer"):
        super().__init__()
        self._name = name
        self.player_type = 'computer'

    def choose(self):
        options = list(self.__class__.CHOICES.values())
        choice = random.choice(options)
        self.move = Move(choice)
        return self.move

class R2D2(Computer):
    def __init__(self):
        super().__init__("R2D2")

    def choose(self):
        return Move("ROCK")

class HAL(Computer):
    def __init__(self):
        super().__init__("HAL")

    def choose(self):
        if random.random() <= .75:
            return Move("SCISSORS")
        return super().choose()

class Daneel(Computer):
    def __init__(self, game):
        super().__init__("Daneel")
        self._game = game

    def choose(self):
        if len(self._game.rounds) == 1:
            return super().choose()
        return self._game.rounds[-2].human_move

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
