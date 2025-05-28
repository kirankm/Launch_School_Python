from utilities import clear_screen, prompt
import random

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
        self._type = None

    def choose(self):
        return NotImplemented
    
    @property
    def move(self):
        return self._move
    
    @move.setter
    def move(self, new_move):
        self._move = new_move

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    def __str__(self):
        return self._name

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self._name = "Kiran"
        self.type = 'human'

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
        self.type = 'computer'

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