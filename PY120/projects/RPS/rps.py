import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../common")))

from game import Game
from rps_tournament import RPSTournament

## Set path to config file
config_path = os.path.join(os.path.dirname(__file__), "rps_config.json")

# Load Game
game = Game("Rock Paper Scissors Lizard Spock", config_path)

# Set Round Type

## Set Tournament Type
rps_tournament = RPSTournament(game, 'rps_config.json')
game.tournament = rps_tournament

## Launch Game
game.start()