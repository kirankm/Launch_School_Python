######
# Import Libraries
import json
import os
import types
import subprocess
import random
import math
import time
import pdb


# Common Functions
def prompt(msg, prefix_space = False):
    if prefix_space:
        print("\n")
    if isinstance(msg, list):
        msg = "\n".join(msg)
    print(f"==> {msg}")

def clear_screen():
    subprocess.run('clear', shell=True, check = True)

def get_valid_input(prompt_msg, error_msg, valid_input):
    prompt(prompt_msg, True)
    while True:
        user_input = input().strip().lower()

        if isinstance(valid_input, types.FunctionType):
            validation_status = valid_input(user_input)
        elif isinstance(valid_input, list):
            validation_status = check_list_validation(user_input, valid_input)
        else:
            valid_input = list(valid_input)
            validation_status = check_list_validation(user_input, valid_input)
        if validation_status:
            return user_input
        prompt(error_msg, prefix_space = True)

def check_list_validation(value_to_check, validation_list):
    return value_to_check.lower() in [x.lower() for x in validation_list]

def check_dict_validation(value_to_check, validation_dict):
    in_keys =  value_to_check.lower() in [
        x.lower() for x in validation_dict.keys()
        ]
    if in_keys:
        return True
    in_values =  value_to_check.lower() in [
        x.lower() for x in validation_dict.values()
        ]
    return in_values

# Pre Load Game Functions
def load_rps_files(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, file_name)

    with open(json_file_path,'r') as f:
        json_file = json.load(f)
    return json_file

################ Introduction
def introduce(menu_options):
    clear_screen()
    intro_msg = RPS_COMMENTS['intro']
    intro_error_msg = RPS_COMMENTS['intro_error']
    user_choice = get_valid_input(intro_msg, intro_error_msg, menu_options)
    return menu_options[user_choice]

############## help screen functions
def show_help_screen(move_choices, winning_moves):
    introduce_help_screen()
    show_shortcut_keys(move_choices)
    show_rules(winning_moves)
    show_additional_options()
    exit_help_screen()

def introduce_help_screen():
    clear_screen()
    prompt(RPS_COMMENTS['help_screen_intro'])

def show_shortcut_keys(choices):
    prompt(RPS_COMMENTS["moves_menu"], prefix_space= True)
    for index, move in enumerate(choices):
        msg = f"Enter {move} for {choices[move]}"
        print(msg)

def show_rules(rules):
    prompt("These are the rules in the Game", prefix_space= True)
    for index, winning_move in enumerate(rules):
        for losing_move, defeating_action in rules[winning_move].items():
            msg = f"{winning_move} {defeating_action} {losing_move}"
            print(msg)
    
def show_additional_options():
    prompt(RPS_COMMENTS['additional_options'], prefix_space= True)

def exit_help_screen():
    exit_msg ="Enter q to return to the main menu"
    get_valid_input(exit_msg, exit_msg, 'q')

################# config screen functions
def edit_config(settings):
    new_config = settings.copy()
    while True: 
        introduce_config_screen()
        edit_config_function = get_config_edit_function(settings)
        if edit_config_function is None:
            break
        edit_config_function(new_config)
    updated_config = remove_redundant_updates(settings, new_config)
    return updated_config

def introduce_config_screen():
    clear_screen()
    prompt(RPS_COMMENTS['config_screen_intro'])

def get_config_edit_function(settings):
    config_options_dict = settings['config_edit_menu']
    config_edit_msg = RPS_COMMENTS['config_screen_options']
    config_error_msg = RPS_COMMENTS['config_screen_invalid_selection']
    config_error_msg += config_edit_msg

    user_choice = get_valid_input(config_edit_msg, config_error_msg, 
                                  config_options_dict)
    config_edit_fn_name = config_options_dict[user_choice]
    config_edit_fn = None if not(config_edit_fn_name) else eval(config_edit_fn_name)
    return config_edit_fn

def show_current_val(settings_file, setting_display_name, setting_key):
    current_setting_value = settings_file[setting_key]
    msg = f"The current {setting_display_name} is {current_setting_value}"
    prompt(msg)
    
def get_new_value_from_options(list_of_options, setting_display_name):
    get_value_msg = f"Choose the new value for {setting_display_name}"
    err_msg = f"Invalid value given for {setting_display_name}. Choose from:"

    choose_msg = "\n".join([f"Press {option[0].lower()} for {option}"
                            for option in list_of_options])
    get_value_msg_full = get_value_msg + "\n" + choose_msg
    err_msg_full = err_msg + "\n" + choose_msg

    valid_user_inputs = [option[0].lower() for option in list_of_options]
    user_input = get_valid_input(get_value_msg_full, err_msg_full, 
                            valid_user_inputs)
    new_value = [val for val in list_of_options 
                 if val[0].lower() == user_input][0]
    return new_value

def get_new_value_from_user(validation_fn, setting_display_name):
    get_value_msg = f"Choose the new value for {setting_display_name}"
    err_msg = f"Invalid value given for {setting_display_name}."
    new_value = get_valid_input(get_value_msg, err_msg, validation_fn)
    return new_value

def edit_ai_personality(new_config):
    clear_screen()
    show_current_val(new_config, "AI Personality", "AI_personality")
    list_of_options = new_config['AI_personality_options']
    user_chosen_value = get_new_value_from_options(list_of_options,
                                                   "AI Personality")
    new_config["AI_personality"] = user_chosen_value

def edit_game_mode(new_config):
    clear_screen()
    show_current_val(new_config, "Game Mode", "game_mode")
    list_of_options = new_config['game_mode_options']
    user_chosen_value = get_new_value_from_options(list_of_options,
                                                   "Game Mode")
    new_config["game_mode"] = user_chosen_value 

def edit_player_name(new_config):
    clear_screen()
    show_current_val(new_config, "Player Name", "name_of_player")
    prompt("Choose the new value for User Name")
    user_chosen_value = get_new_value_from_user(is_len_gt_0,
                                                "Player Name")
    new_config["name_of_player"] = user_chosen_value 
    
def is_len_gt_0(string):
    return len(string) > 0

def edit_game_path(new_config):
    clear_screen()
    show_current_val(new_config, "PATH TO GAME HISTORY", "game_history_path")
    prompt("Choose the new value for Path to Game History")
    user_chosen_value = get_new_value_from_user(is_valid_path,
                                                "PATH TO GAME HISTORY")
    new_config["game_history_path"] = user_chosen_value

def is_valid_path(path):
    return os.path.exists(path)

def edit_no_of_rounds(new_config):
    clear_screen()
    show_current_val(new_config, "Number of Rounds", "no_of_rounds")
    prompt("Choose the new value for Number of Rounds")
    user_chosen_value = get_new_value_from_user(is_valid_int,
                                                "Number of Rounds")
    new_config["no_of_rounds"] = int(user_chosen_value)

def is_valid_int(string):
    return string.strip().isdigit() and string.strip() != ''

def remove_redundant_updates(settings, new_config):
    return {
        setting:new_config[setting]
        for setting in new_config
        if new_config[setting] != settings[setting]
    }

def update_and_save_config(current_settings, updated_settings):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, "rps_config.json")

    new_settings = current_settings | updated_settings
    with open(json_file_path,'w') as f:
        json.dump(new_settings, f, indent = 2)

############################# new game functions
def start_new_game(move_choice, winning_moves, no_of_rounds):
    new_game_introduction()
    score = {'user': 0 , 'computer': 0}
    while should_continue_playing(score, no_of_rounds):
        round_winner = play_new_round(move_choice, winning_moves, score)
        update_score(score, round_winner)
        should_continue(score)
    display_final_result(score)

def new_game_introduction():
    intro_msg = RPS_COMMENTS['new_game_intro']
    clear_screen()
    prompt(intro_msg)

def should_continue_playing(curr_score, total_rounds):
    cutoff = math.ceil(total_rounds / 2)
    return (curr_score['user'] < cutoff) and (curr_score['computer'] < cutoff)

def update_score(score_dict, winner):
    if winner in score_dict:
        score_dict[winner] += 1

def should_continue(score):
    display_current_score(score)
    input("press enter to continue to next round:")

def display_final_result(score_dict):
    if score_dict['user'] > score_dict['computer']:
        print("User has Won")
    else:
        print("Computer has Won")

def play_new_round(move_choice, winning_moves, score):
    new_round_introduction()
    display_current_score(score)
    user_move = get_user_move(move_choice)
    computer_move = get_computer_move(move_choice)
    winner = identify_winner(user_move, computer_move, winning_moves)
    display_round_result(winner, user_move, computer_move)
    return winner

def new_round_introduction():
    intro_msg = RPS_COMMENTS['new_game_intro']
    clear_screen()
    prompt(intro_msg)

def display_current_score(score):
    prompt(score)

def get_user_move(moves):
    choose_msg  = RPS_COMMENTS['human_move_choose']
    list_choice_msg = '\n'.join([f'{key} for {val}' for key, val in moves.items()])
    comb_msg = choose_msg + '\n' + list_choice_msg + "\n"

    invalid_choice_msg = RPS_COMMENTS['human_move_error'] 
    invalid_choice_msg = invalid_choice_msg + '\n' + list_choice_msg + "\n"

    user_choice = get_valid_input(comb_msg, invalid_choice_msg, moves)
    user_move = moves[user_choice]
    display_move("user", user_move)
    return user_move

def get_computer_move(choices):
    list_of_moves = list(choices.values())
    computer_move = random.choice(list_of_moves)
    display_move("computer", computer_move)
    return computer_move

def identify_winner(user_move, computer_move, winning_moves):
    if computer_move in winning_moves[user_move]:
        return "user"
    elif user_move in winning_moves[computer_move]:
        return "computer"
    else:
        return None

def display_round_result(result, user_move, computer_move):
    if result is None:
        msg = f"User and computer have both chosen {user_move}"
        prompt(RPS_COMMENTS["tie"])
    elif result == "user":
        msg = f"Users {user_move} has defeated the computer's {computer_move}"
        prompt(msg, prefix_space= True)
        prompt(RPS_COMMENTS['user_wins'])
    else:
        msg = f"Users {user_move} has lost to the computer's {computer_move}"
        prompt(msg, prefix_space= True)
        prompt(RPS_COMMENTS['computer_wins'])

## common new game functions
def display_move(user, move):
    msg = f'{RPS_COMMENTS[f'{user}_move']}{move}'
    prompt(msg)

#################### quit game functions
def quit_game():
    clear_screen()
    prompt(RPS_COMMENTS["exit_game"])
    time.sleep(2)

# high score functions
def show_high_scores():
    pass

# Pre Load Game Files and Variables
RPS_SETTINGS = load_rps_files("rps_config.json")

PERSONALITY = RPS_SETTINGS['AI_personality']
NO_OF_ROUNDS = RPS_SETTINGS["no_of_rounds"]
PLAYER_NAME = RPS_SETTINGS["name_of_player"]
GAME_MODE = RPS_SETTINGS["game_mode"]
GAME_HISTORY_PATH = RPS_SETTINGS['game_history_path']
MOVE_CHOICE = RPS_SETTINGS['move_choice']
WINNING_MOVES = RPS_SETTINGS['rules']
MAIN_SCREEN_OPTIONS = RPS_SETTINGS['main_screen_menu']

RPS_COMMENTS = load_rps_files("rps_comments.json")[PERSONALITY]

############ Program Flow
while True:
    user_introduction_choice = introduce(MAIN_SCREEN_OPTIONS)
    match user_introduction_choice:
        case 'help':
            show_help_screen(MOVE_CHOICE, WINNING_MOVES)
        case 'high_score':
            show_high_scores()
        case 'config':
            updated_config = edit_config(RPS_SETTINGS)
            if updated_config:
                update_and_save_config(RPS_SETTINGS, updated_config)
                prompt(RPS_COMMENTS['save_config_exit'])
                break
        case 'new_game':
            start_new_game(MOVE_CHOICE, WINNING_MOVES, NO_OF_ROUNDS)
        case 'quit_game':
            quit_game()
            break
