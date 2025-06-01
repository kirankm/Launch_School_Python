from utilities import get_user_input, prompt, clear_screen, replace_last
from config import StringConfig, IntConfig, BoolConfig, PathConfig

import pdb
class Menu:
    def __init__(self, new_game, options):
        self._game = new_game
        self._options = options

    def display(self):
        clear_screen(self._game.name)
        self._display_intro()
        user_choice = self._get_user_choice()
        self._handle_user_choice(user_choice)

    def _display_intro(self):
        return NotImplemented

    def _get_user_choice(self):
        options = list(self._options)
        if 'q' not in options:
            options.append('q')
        intro_msg = self._list_options()
        error_msg = f"Invalid choice. Choose from {', '.join(options)}"
        error_msg = replace_last(error_msg, ',', " or ")
        choices = tuple(options)
        return get_user_input(intro_msg, error_msg, choices)

    def _list_options(self):
        return "\n".join([self._display_option(option)
                                for option in self._options])
    
    def _display_option(self, option):
        option_info = self._options[option]
        if isinstance(option_info, dict):
            option_info = option_info['desc']
        return f"\tEnter {option} to {option_info}"

    def _handle_user_choice(self, user_choice):
        return NotImplemented

class MainMenu(Menu):
    def __init__(self, new_game, options):
        super().__init__(new_game, options)
    
    def _display_intro(self):
        prompt(f"Welcome to the {self._game.name} game", prefix_space= True)

    def _handle_user_choice(self, user_choice):
        match user_choice:
            case 'n':
                self._game.tournament.play()
            case 'h':
                self._game.display_help()
            case 'c':
                self._game.config_menu.display()
            case 'd':
                self._game.display_stats()
            case 'q':
                self._game.quit()

class ConfigMenu(Menu):
    def __init__(self, new_game, options):
        super().__init__(new_game, options)
    
    def _display_intro(self):
        line_1 = f"Welcome to the {self._game.name} Config Screen"
        line_2 = "Here you can edit the followings settings in the game"
        prompt(line_1, prefix_space= True)
        prompt(line_2)

    def _list_options(self):
        configurable_options =  super()._list_options()
        quit_option = "\tEnter q to go back to main menu"
        return configurable_options + "\n\n" + quit_option

    def _handle_user_choice(self, user_choice):
        match user_choice:
            case 'q':
                self._game.main_menu.display()
            case _:
                config_dict = self._options[user_choice]
                data_type = config_dict['type']
                config = self._get_config_type(data_type)
                new_config = config(user_choice, config_dict, self._game)
                new_config.get_new_value()

    def _get_config_type(self, config_type):
        match config_type:
            case "string":
                return StringConfig
            case "int":
                return IntConfig
            case "boolean":
                return BoolConfig
            case "path":
                return PathConfig