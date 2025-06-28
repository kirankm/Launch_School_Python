from utilities import prompt, get_user_input, clear_screen
from pathlib import Path

class Config:
    def __init__(self, key, config_dict, game):
        self._game = game
        self._value = key
        self._config_dict = config_dict

    @property
    def description(self):
        return self._config_dict['desc']
    
    @property
    def curr_val(self):
        return self._config_dict['curr_val']

    @curr_val.setter
    def curr_val(self, new_value):
        self._config_dict['curr_val'] = new_value

    def _process_input(self,value):
        return value

    def get_new_value(self):
        clear_screen(self._game.name)
        self._display_intro()
        user_choice = self._get_user_choice(self._process_input)
        self._handle_user_choice(user_choice)

    def _display_intro(self):
        prompt(f"You have chosen to {self.description}")
        prompt(f"The Current Value is {self.curr_val}")

    def _get_user_choice(self, proc_fn = None):
        intro_msg = self._get_intro_msg()
        error_msg = self._get_error_msg()
        return get_user_input(intro_msg, error_msg, self._is_valid, proc_fn)

    def _get_intro_msg(self):
        line_1 = f"Give the new value"
        if "intro_text" in self._config_dict:
            line_1 = self._config_dict['intro_text']
        line_2 = "Or enter q to go back to the main menu"
        return line_1 + "\n" + line_2

    def _get_error_msg(self):
        return NotImplemented

    def _is_valid(self):
        return NotImplemented
    
    def _handle_user_choice(self, choice):
        if not(isinstance(choice, str)) or (choice.lower() != "q"):
            self.curr_val = choice
        self._game.config_menu.display()

class StringConfig(Config):
    def __init__(self, key, config_dict, new_game):
        super().__init__(key, config_dict, new_game)

    def _process_input(self, value):
        return str.capitalize(value)

    def _get_error_msg(self):
        return "Empty Strings are not allowed. Try agian!!"
    
    def _is_valid(self, value):
        return len(value) > 0
    
class IntConfig(Config):
    def __init__(self, key, config_dict, new_game):
        super().__init__(key, config_dict, new_game)

    def _get_error_msg(self):
        return "Only integer values are allowed. Try agian!!"
    
    def _process_input(self, value):
        try:
            return int(value)
        except:
            return value
    
    def _is_valid(self, value):
        if isinstance(value, str) and value.lower() == "q":
            return True
        try:
            int(value)
            return True
        except ValueError:
            return False
        
class BoolConfig(Config):
    def __init__(self, key, config_dict, new_game):
        super().__init__(key, config_dict, new_game)

    def _get_user_choice(self):
        return super()._get_user_choice(self._process_input)

    def _process_input(self, value):
        if value.lower() in ['t', 'true']:
            return True
        elif value.lower() in ['f', 'false']:
            return False
        return value

    def _get_error_msg(self):
        return "Only t/true or f/false is allowed. Try again!!!"

    def _is_valid(self, value):
        if isinstance(value, bool):
            return True
        return value.lower() == "q"

class PathConfig(Config):
    def __init__(self, key, config_dict, new_game):
        super().__init__(key, config_dict, new_game)

    def _get_error_msg(self):
        return "Only valid Json files are allowed. Try again!!"
        
    def _is_valid(self, value):
        if value.lower() == "q":
            return True
        return value.lower().endswith(".json")
            