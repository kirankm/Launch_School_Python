from utilities import clear_screen, wave_hands_bye, load_json_file, prompt
from menu import MainMenu, ConfigMenu

class Game:
    def __init__(self, name, config):
        self._tournament = None
        self.config = config
        self._main_menu = MainMenu(self, self.config['main_menu'])
        self._config_menu = ConfigMenu(self, self.config['config_menu'])
        self._name = name

    def listen_for_keys(self, key_list):
        user_key = input()
        return user_key if user_key in list(key_list) else False
    
    @property
    def name(self):
        return self._name.title()

    @property
    def config(self):
        return self._config
    
    @config.setter
    def config(self, config_file):
        try:
            self._config = load_json_file(config_file)
        except FileNotFoundError:
            prompt("The config file could not be found")
            self._config = {}

    @property
    def tournament(self):
        return self._tournament
    
    @tournament.setter
    def tournament(self, tournament):
        self._tournament = tournament
    
    @property
    def main_menu(self):
        return self._main_menu
    
    @property
    def config_menu(self):
        return self._config_menu

    def start(self):
        self.main_menu.display()

    def display_help(self):
        clear_screen(self.name)
        no_help_text = "No help file given"
        help_text = self.config.get("game_rules", no_help_text)
        prompt(help_text)
        prompt("Press q to go back to the main menu", prefix_space= True)
    
    def display_stats(self):
        pass

    def quit(self):
        clear_screen(self.name)
        wave_hands_bye(self.name)
        clear_screen()

# game = Game("Tic Tac Toe", "config.json")
# game.start()
