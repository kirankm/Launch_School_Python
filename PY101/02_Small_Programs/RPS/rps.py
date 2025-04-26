######
# Import Libraries
import json
import os
import types
import subprocess
import random
import math
import time
import shutil

# Common Functions
def prompt(msg, prefix_space = False):
    if prefix_space:
        print("\n")
    if isinstance(msg, list):
        msg = "\n".join(msg)
    print(f"==> {msg}")

def clear_screen(banner = True):
    subprocess.run('clear', shell=True, check = True)
    if banner:
        display_game_banner()

def display_game_banner():
    terminal_width = shutil.get_terminal_size().columns
    line1 = "*"*terminal_width
    line2 = f"*{' '*(terminal_width-2)}*"
    game_name = 'ROCK PAPER SCISSORS LIZARD SPOCK'.center(terminal_width - 2)
    line3 = f"*{game_name}*"
    banner = [line1, line2, line3, line2, line1]
    print("\n".join(banner))

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

def write_to_json_file(file_path, value):
    with open(file_path,'w') as f:
        json.dump(value, f, indent = 2)

def load_json_file(json_file_path):
    with open(json_file_path,'r') as f:
        loaded_file = json.load(f)
    return loaded_file

def get_json_file_path(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    _, ext = os.path.splitext(file_name)
    if ext == '':
        file_name += ".json"
    json_file_path = os.path.join(script_dir, file_name)
    return json_file_path

# Pre Load Game Functions
def load_rps_files(file_name):
    json_file_path = get_json_file_path(file_name)
    return load_json_file(json_file_path)

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
    prompt(RPS_COMMENTS['help_screen_intro'], prefix_space= True)

def show_shortcut_keys(choices):
    prompt(RPS_COMMENTS["moves_menu"], prefix_space= True)
    for move in choices:
        msg = f"Enter {move} for {choices[move]}"
        print(msg)

def show_rules(rules):
    prompt("These are the rules in the Game", prefix_space= True)
    for winning_move in rules:
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
    final_config = remove_redundant_updates(settings, new_config)
    return final_config

def introduce_config_screen():
    clear_screen()
    prompt(RPS_COMMENTS['config_screen_intro'])

def get_config_edit_function(settings):
    config_options_dict = settings['config_edit_menu'].copy()
    config_edit_msg = RPS_COMMENTS['config_screen_options'].copy()
    config_error_msg = RPS_COMMENTS['config_screen_invalid_selection'].copy()
    config_error_msg += config_edit_msg

    user_choice = get_valid_input(config_edit_msg, config_error_msg,
                                  config_options_dict)
    config_edit_fn_name = config_options_dict[user_choice]
    if config_edit_fn_name:
        return eval(config_edit_fn_name)
    return None

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
    prompt(["Choose the new value for User Name.",
            "Leading and Lagging white spaces will be removed",
            "Names longer than 32 characters will be truncated"
            ])
    user_chosen_value = get_new_value_from_user(is_len_gt_0,
                                                "Player Name")
    user_chosen_value = user_chosen_value.strip()[:32]
    new_config["name_of_player"] = user_chosen_value.capitalize()

def is_len_gt_0(string):
    return len(string.strip()) > 0

def edit_game_history_file(new_config):
    clear_screen()
    show_current_val(new_config, "GAME HISTORY FILE", "game_history_filename")
    prompt("Choose the new value for Path to Game History")
    user_chosen_value = get_new_value_from_user(is_valid_filename,
                                                "GAME HISTORY FILE")
    new_config["game_history_filename"] = user_chosen_value

def is_valid_filename(name):
    if not name or name in {'.', '..'}:
        return False

    invalid_chars = r'<>:"/\\|?*\0'
    if any(char in name for char in invalid_chars):
        return False

    return True

def edit_no_of_rounds(new_config):
    clear_screen()
    show_current_val(new_config, "Number of Rounds", "no_of_rounds")
    prompt(["Choose the new value for Number of Rounds",
            "Only Odd Numbers are allowed"
            ])
    user_chosen_value = get_new_value_from_user(is_valid_int,
                                                "Number of Rounds")
    new_config["no_of_rounds"] = int(user_chosen_value)

def is_valid_int(string):
    if string.strip().isdigit() and string.strip() != '':
        return int(string) %2 ==  1
    return False

def remove_redundant_updates(settings, new_config):
    return {
        setting:new_config[setting]
        for setting in new_config
        if new_config[setting] != settings[setting]
    }

def update_and_save_config(current_settings, updated_settings):
    json_file_path = get_json_file_path("rps_config.json")

    new_settings = current_settings | updated_settings
    with open(json_file_path,'w') as f:
        json.dump(new_settings, f, indent = 2)

############################# new game functions
def start_new_game(settings):
    player_name = settings["name_of_player"].capitalize()
    new_game_introduction(player_name, settings)
    history = initialize_game_history(settings, player_name)

    play_new_tournament(history, settings, player_name)
    display_final_result(history, settings["no_of_rounds"], player_name)

    if not check_game_incomplete(history, settings["no_of_rounds"]):
        save_game_history(settings, history)
    return should_play_again() == "y"

def new_game_introduction(user_name, settings):
    intro_msg = RPS_COMMENTS['new_game_intro'].replace('user', user_name)
    clear_screen()
    prompt(intro_msg)
    display_current_game_settings(user_name, settings)

def display_current_game_settings(user_name, settings):
    current_no_of_rounds = settings["no_of_rounds"]
    current_ai_personality = settings["AI_personality"]
    current_game_mode = settings["game_mode"]
    prompt(f"Current Player Name is {user_name}", prefix_space = True)
    prompt(f"Current Number of Rounds in a game is {current_no_of_rounds}")
    prompt(f"Current personality of the AI is {current_ai_personality}")
    prompt(f"Current game mode is {current_game_mode}")
    prompt("Go to Config from Main Menu to edit these settings", True)

def initialize_game_history(settings, player_name):
    game_history = {'user': 0 , 'computer': 0, 'last_match':None}
    game_history['game_mode'] = settings['game_mode']
    game_history['AI_personality'] = settings['AI_personality']
    game_history['no_of_rounds'] = settings['no_of_rounds']
    game_history['player_name'] = player_name
    game_history['moves'] = []
    return game_history

def play_new_tournament(history, settings, player_name):
    while check_game_incomplete(history, settings["no_of_rounds"]):
        play_new_round(settings, history, player_name)
        continue_next_round = should_continue_next_round(history,
                                                    settings["no_of_rounds"])
        if continue_next_round == 'q':
            break

def check_game_incomplete(curr_history, total_rounds):
    cutoff = math.ceil(total_rounds / 2)
    return (curr_history['user'] < cutoff) and \
            (curr_history['computer'] < cutoff)

def should_continue_next_round(curr_history, no_of_rounds):
    if (check_game_incomplete(curr_history, no_of_rounds)):
        if curr_history['last_match'] != 'tie':
            msg = RPS_COMMENTS['continue_round_win']
        else:
            msg = RPS_COMMENTS['continue_round_tie']
        prompt(msg, prefix_space = True)
        user_input = input()
        return user_input
    return None

def display_final_result(game_history, no_of_rounds, user_name):
    if check_game_incomplete(game_history, no_of_rounds):
        final_msg = RPS_COMMENTS['user_quit_early']
    elif game_history['user'] > game_history['computer']:
        final_msg = RPS_COMMENTS['user_won']
        win_msg = f" by winning {game_history['user']} rounds"
        final_msg += win_msg
    else:
        final_msg = RPS_COMMENTS['user_lost']
        win_msg = f" by winning {game_history['computer']} rounds"
        final_msg += win_msg
    prompt(final_msg.replace('User', user_name), True)

def should_play_again():
    input_msg = RPS_COMMENTS["play_tournament_again"]
    error_msg = RPS_COMMENTS["play_tournament_invalid_input"]
    user_choice = get_valid_input(input_msg, error_msg,
                                  validate_should_continue)
    return user_choice[0].lower() ## Make comment based on win or loss

def validate_should_continue(user_input):
    valid_values = ['yes', 'y', 'no', 'n']
    return user_input.lower() in valid_values

def play_new_round(settings, game_history, user_name):
    new_round_introduction(game_history, settings["no_of_rounds"], user_name)
    user_move = get_user_move(settings['move_choice'], user_name)
    computer_move = get_computer_move(settings['move_choice'],
                                      settings['game_mode'], user_move)
    winner = identify_winner(user_move, computer_move, settings['rules'])
    display_round_result(winner, user_move, computer_move, settings['rules'],
                        user_name)
    update_game_history(game_history, user_move, computer_move, winner)
    return winner

def new_round_introduction(game_history, total_rounds, user_name):
    intro_msg = RPS_COMMENTS['new_round_intro']
    total_games = game_history['user'] + game_history['computer']
    intro_msg = f"{intro_msg}{total_games + 1}"
    if (game_history['last_match'] in ['user', 'computer']):
        clear_screen()
    if game_history['last_match'] != 'tie':
        prompt(intro_msg, prefix_space = True)
        display_current_score(game_history, total_rounds, user_name)


def display_current_score(history, total_rounds, user_name):
    if history['user'] + history['computer'] == 0:
        summary = "Current Score: user : 0, Computer : 0"
    else:
        leader, lagger = get_leader_lagger(history)
        games_remaining = get_games_remaing(total_rounds, history)

        if leader:
            lead = get_lead(history)
            summary = "".join([
                f"{leader} leads {lagger} by ",
                f"{lead} with {games_remaining} remaining."
            ])
        else:
            games_won = get_games_won(history)
            summary = "".join([
                f"With {games_remaining} to go, the game is tied with ",
                f"each player winning {games_won}."
            ]).capitalize()

    print(summary.replace('user', user_name))

def get_leader_lagger(history):
    if history['user'] > history['computer']:
        return 'user', 'Computer'
    if history['user'] < history['computer']:
        return 'Computer', 'user'
    return None, None

def get_games_remaing(total_rounds, history):
    game_remaining = total_rounds - history['user'] - history['computer']
    game_remaing_suffix =  'games' if game_remaining > 1 else 'game'
    return f'{game_remaining} {game_remaing_suffix}'

def get_lead(history):
    lead = abs(history['user'] - history['computer'])
    lead_suffix =  'points' if lead > 1 else 'point'
    return f'{lead} {lead_suffix}'

def get_games_won(history):
    games_won = history['user']
    games_won_suffix = 'games' if games_won > 1 else 'game'
    return f'{games_won} {games_won_suffix}'

def get_user_move(moves, user_name):
    choose_msg  = RPS_COMMENTS['human_move_choose']
    list_choice_msg = '\n'.join([f'{key} for {val}'
                                 for key, val in moves.items()])
    comb_msg = choose_msg + '\n' + list_choice_msg + "\n"

    invalid_choice_msg = RPS_COMMENTS['human_move_error']
    invalid_choice_msg = invalid_choice_msg + '\n' + list_choice_msg + "\n"

    user_choice = get_valid_input(comb_msg, invalid_choice_msg, moves)
    user_move = moves[user_choice]
    display_move("user", user_move, user_name)
    return user_move

def get_computer_move(choices, game_mode = None, user_move = None):
    list_of_moves = list(choices.values())
    if game_mode == "No Tie":
        user_move_index = list_of_moves.index(user_move)
        list_of_moves.pop(user_move_index)
    computer_move = random.choice(list_of_moves)
    display_move("computer", computer_move)
    return computer_move

def identify_winner(user_move, computer_move, winning_moves):
    if user_move == computer_move:
        return None
    if computer_move in winning_moves[user_move]:
        return "user"
    return "computer"

def display_round_result(winner, user_move, computer_move, winning_moves,
                         user_name):
    if winner is None:
        move_msg = f"user and Computer have both chosen {user_move}"
        result_msg = RPS_COMMENTS["tie"]
    elif winner == "user":
        action = winning_moves[user_move][computer_move]
        move_msg = f"user's {user_move} {action} computer's {computer_move}"
        result_msg = RPS_COMMENTS['user_wins'].replace('user', user_name)
    else:
        action = winning_moves[computer_move][user_move]
        move_msg = f"Computer's {computer_move} {action} user's {user_move}"
        result_msg = RPS_COMMENTS['computer_wins']
    move_msg = move_msg.replace('user', user_name)
    prompt(move_msg, prefix_space = True)
    prompt(result_msg)

def update_game_history(history, user_move, computer_move, winner):
    update_history_moves(history, user_move, computer_move)
    update_history_winner(history, winner)

def update_history_moves(history, user_move, computer_move):
    game_dict = {'user': user_move, 'computer': computer_move}
    if history['last_match'] == 'tie':
        history['moves'][-1].append(game_dict)
    else:
        history['moves'].append([game_dict])

def update_history_winner(curr_history, winner):
    if winner in curr_history:
        curr_history[winner] += 1
        curr_history['last_match'] = winner
    else:
        curr_history['last_match'] = "tie"

## common new game functions
def display_move(user, move, user_name = None):
    prefix_space = user == "user"
    msg = f'{RPS_COMMENTS[f'{user}_move']}{move}'
    if user_name:
        msg = msg.replace('user', user_name)
    prompt(msg, prefix_space = prefix_space)

## Create Game History functions
def save_game_history(settings, history):
    file_name = settings['game_history_filename']
    json_file_path = get_game_history_path(file_name)
    append_history_to_file(json_file_path, history)
    return json_file_path

def get_game_history_path(file_name):
    json_file_path = get_json_file_path(file_name)

    if not(os.path.exists(json_file_path)):
        write_to_json_file(json_file_path, [])
    return json_file_path

def append_history_to_file(json_file_path, history):
    prev_history = load_json_file(json_file_path)
    prev_history.append(history)
    write_to_json_file(json_file_path, prev_history)

## Create Stats Functions
def display_user_stats(settings):
    sort_function, reverse = (None, True)
    history = load_game_history(settings)
    while True:
        give_user_stats_intro()
        user_perf = get_user_perf(history)
        user_stats = {user:get_user_stats(result)
                      for user, result in user_perf.items()}
        sel_players = get_selected_players(user_stats, sort_function, reverse)
        pretty_print(user_stats, sel_players)
        sort_function, reverse = get_table_sort_params(sort_function, reverse)
        if (sort_function is None) and (reverse is None):
            break
    return user_stats

def load_game_history(settings):
    file_name = f"{settings['game_history_filename']}.json"
    return load_rps_files(file_name)

def give_user_stats_intro():
    clear_screen()
    msg = RPS_COMMENTS["user_stats_intro"]
    prompt(msg)

def get_user_perf(history):
    user_performance = {}
    for match in history:
        player = match['player_name']
        winner = match['last_match']
        user_performance.setdefault(player, [])
        user_performance[player].append(winner)
    return user_performance

def get_user_stats(user_perf):
    return {player:user_perf.count(player) for player in set(user_perf)}

def pretty_print(user_statistics, sel_players):
    print("\n")
    print_table_header()
    for player in sel_players:
        print_user_result_row(user_statistics, player)

def get_selected_players(user_statistics, sort_fn = None, reverse = True,
                                                            top_n = 5):
    match sort_fn:
        case "w":
            def sort_win(x):
                return user_statistics[x].get('user', 0)
            sort_fn = sort_win
        case 'g':
            def sort_games(x):
                return user_statistics[x].get('user', 0) + \
                                user_statistics[x].get('computer', 0)
            sort_fn = sort_games
        case 'p':
            def sort_win_perc(x):
                return user_statistics[x].get('user', 0) / \
                                (user_statistics[x].get('computer', 0) +
                                 user_statistics[x].get('user', 0))
            sort_fn = sort_win_perc
    if sort_fn:
        sorted_players = sorted(user_statistics, key = sort_fn,
                                reverse = reverse)
    else:
        sorted_players = sorted(user_statistics, reverse = reverse)
    return sorted_players[:top_n]

def get_table_sort_params(curr_sort_fn, curr_reverse):
    sort_table_msg = RPS_COMMENTS['sort_table']
    sort_table_err = RPS_COMMENTS['sort_table_error']
    valid_input = ['w', 'g', 'p', 'q', 'r']
    sort_table_user_choice = get_valid_input(sort_table_msg, sort_table_err,
                                                valid_input)
    sort_fn, reverse = get_sort_params(sort_table_user_choice,
                                        curr_sort_fn, curr_reverse)
    return sort_fn, reverse

def get_sort_params(choice, curr_sort_fn, curr_reverse):
    match choice:
        case 'w':
            return 'w', True
        case 'p':
            return 'p', True
        case 'g':
            return 'g', True
        case 'r':
            return curr_sort_fn, not(curr_reverse)
        case 'q':
            return None, None

def print_table_header():
    line0 = (27*"*-").center(55)[:54]
    col1 = 'Name'.center(15)
    col2 = 'Wins'.center(15)
    col3 = 'Losses'.center(15)
    line1 = f"| {col1} | {col2} | {col3} |"
    line2 = (27*"*-").center(55)[:54]

    print(line0)
    print(line1)
    print(line2)

def print_user_result_row(all_win_stats, user_name):
    display_name = user_name[:15].center(15)
    user_data = all_win_stats[user_name]
    wins = str(user_data.get('user', 0)).center(15)
    loss = str(user_data.get('computer', 0)).center(15)
    line1 = f"| {display_name} | {wins} | {loss} |"
    line2 = (27*"*-").center(55)[:54]
    print(line1)
    print(line2)

#################### quit game functions
def quit_game():
    clear_screen()
    wave_hands_bye()
    clear_screen(banner = False)

def wave_hands_bye():
    frames = [
    r"""
    \o  
     |  
    / \ 
    """,
    r"""
     o/ 
     |  
    / \ 
    """
    ]

    for _ in range(6):
        for frame in frames:
            clear_screen()
            prompt(RPS_COMMENTS["exit_game"])
            print(frame)
            time.sleep(0.2)

# Pre Load Game Files and Variables
RPS_SETTINGS = load_rps_files("rps_config.json")

PERSONALITY = RPS_SETTINGS['AI_personality']
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
        case 'display_stats':
            display_user_stats(RPS_SETTINGS)
        case 'config':
            updated_config = edit_config(RPS_SETTINGS)
            if updated_config:
                update_and_save_config(RPS_SETTINGS, updated_config)
                prompt(RPS_COMMENTS['save_config_exit'])
                break
        case 'new_game':
            while True:
                continue_game = start_new_game(RPS_SETTINGS)
                if not(continue_game):
                    break
        case 'quit_game':
            quit_game()
            break
