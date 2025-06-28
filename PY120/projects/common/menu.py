from utilities import get_user_input, prompt, clear_screen, replace_last
from config import StringConfig, IntConfig, BoolConfig, PathConfig

import pdb
class Menu:
    def __init__(self, new_game, options):
        self._game = new_game
        self._options = options

    @property 
    def options(self):
        return self._options

    def display(self):
        clear_screen(self._game.name)
        self._display_intro()
        user_choice = self._get_user_choice()
        self._handle_user_choice(user_choice)

    def _display_intro(self):
        return NotImplemented

    def _get_user_choice(self):
        choices = self._get_list_of_choices()
        intro_msg = self._list_options()
        error_msg = f"Invalid choice. Choose from {', '.join(choices)}"
        error_msg = replace_last(error_msg, ',', " or ")
        return get_user_input(intro_msg, error_msg, choices)

    def _get_list_of_choices(self):
        return list(self._options)

    def _list_options(self):
        return "\n".join([self._display_option(option)
                                for option in self._options])
    
    def _display_option(self, option):
        option_info = self._options[option]
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
                while True:
                    self._game.display_help()
                    if self._game.listen_for_keys('q'):
                        break
                self.display()
            case 'c':
                self._game.config_menu.display()
            case 'd':
                self._game.display_stats()
            case 'q':
                self._game.quit()

class ConfigMenu(Menu):
    def __init__(self, new_game, options):
        super().__init__(new_game, options)
        self._shortcut_map = self._get_shortcut_map()

    @property
    def options(self):
        return self._options
    
    @options.setter
    def options(self, options):
        self._options = {}
        for option_name in options:
            pass

    def _get_shortcut_map(self):
        return {val['shortcut']:key for key,val in self._options.items()}

    def _display_intro(self):
        line_1 = f"Welcome to the {self._game.name} Config Screen"
        line_2 = "Here you can edit the followings settings in the game"
        prompt(line_1, prefix_space= True)
        prompt(line_2)

    def _list_options(self):
        configurable_options =  super()._list_options()
        quit_option = "\tEnter q to go back to main menu"
        return configurable_options + "\n\n" + quit_option

    def _get_list_of_choices(self):
        #options = [config['shortcut'] for _, config in self.options.items()]
        options = list(self._shortcut_map)
        if 'q' not in options:
            options.append('q')
        return options
    
    def _display_option(self, option):
        option_name = self._options[option]['shortcut']
        option_info = self._options[option]['desc']
        return f"\tEnter {option_name} to {option_info}"
    
    def _handle_user_choice(self, user_choice):
        if user_choice == "q":
            self._game.main_menu.display()
        else:
            user_choice = self._shortcut_map[user_choice]
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