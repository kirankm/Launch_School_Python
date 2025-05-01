# Introduce the game
# Initialize the board
#   Display the board
# While moves remain, game not over
    # Get current player
    # Get player_move
    # Update board
# Display result
# Continue Playing

# Import Libraries
import json
import os
import types
import subprocess
import random
import math
import time
import shutil
import pdb

# GAME CONSTANTS
JSON_INDENT = 2
PERSONALITY = "Normal"
GAME_NAME = "TIC TAC TOE"

CELL_HEIGHT = 3
CELL_WIDTH = 5
ROW_DIVIDER = "-"
COL_DIVIDER = "|"

USER_MARKER = 'X'
COMPUTER_MARKER = "O"

# Common Functions
def prompt(msg, prefix_space = False):
    if prefix_space:
        print("\n")
    if isinstance(msg, list):
        msg = "\n".join(msg)
    print(f"==> {msg}")

def clear_screen(game_name = None):
    subprocess.run('clear', shell=True, check = True)
    if game_name:
        display_game_banner(game_name)

def display_game_banner(name):
    terminal_width = shutil.get_terminal_size().columns
    line1 = "*"*terminal_width
    line2 = f"*{' '*(terminal_width-2)}*"
    game_name = name.upper().center(terminal_width - 2)
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
    return value_to_check.lower() in [str(x).lower() for x in validation_list]

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
        json.dump(value, f, indent = JSON_INDENT)

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

# Display Table Functions
def get_cell_line(cell_width, value = None):
    if value is None:
        value = " "
    return f"{value}".center(cell_width)

def get_row_line(row, cell_width, separator):
    row = [None] * 3 if row is None else row
    row_cells = [get_cell_line(cell_width, val) for val in row]
    return separator.join(row_cells)

def get_row(row_values, width, height, separator):
    row = [get_row_line(None, width, separator) for val in range(height)]
    mid_value = (height // 2) 
    row[mid_value] = get_row_line(row_values, width, separator)
    return "\n".join(row)

def get_row_separator(width, separator):
    return ' '.join([separator * width] * 3)

def display_board(data):
    full_row_divider = get_row_separator(CELL_WIDTH, ROW_DIVIDER)
    rows = [get_row(row, CELL_WIDTH, CELL_HEIGHT, COL_DIVIDER) for row in data]
    rows.insert(1, full_row_divider)
    rows.insert(-1, full_row_divider)
    print("\n".join(rows))

# Introduction
def introduce_game():
    clear_screen(GAME_NAME)
    prompt(COMMENTS['game_intro'], prefix_space = True)

def initialize_board():
    return [[None, None, None] for _ in range(3)]

def get_user_move(board):
    prompt_msg = COMMENTS['user_move_choose']
    error_msg = COMMENTS['user_move_choose_invalid']
    valid_moves = get_empty_cells(board)
    user_move = get_valid_input(prompt_msg, error_msg, valid_moves)
    return int(user_move)

def get_computer_move(board):
    valid_moves = get_empty_cells(board)
    computer_move = random.choice(valid_moves)
    return computer_move

def update_board(player, board, move):
    marker = USER_MARKER if player == "user" else COMPUTER_MARKER
    row, col = conv_num_to_cell_address(move)
    board[row][col] = marker

def conv_num_to_cell_address(num):
    num = num - 1 ## Curr Numbers are in 1 to 9, we need it be from 0 to 8
    row = num // 3
    col = num % 3
    return (row, col)

def get_empty_cells(board):
    empty_cells = []
    for num in range(1, 10):
        row, col = conv_num_to_cell_address(num)
        if board[row][col] is None:
            empty_cells.append(num)
    return empty_cells

# Check Game Over Functions
def check_game_over(board):
    return check_squares_finished(board) or check_someone_won(board)

def check_squares_finished(board):
    empty_squares = get_empty_cells(board)
    return len(empty_squares) == 0

def check_someone_won(board):
    return check_rows(board) or check_cols(board) or check_diag(board)

def check_rows(board):
    row_1, row_2, row_3 = board
    return check_arr(row_1) or check_arr(row_2) or check_arr(row_3)

def check_cols(board):
    col_1, col_2, col_3 = list(zip(*board))
    return check_arr(col_1) or check_arr(col_2) or check_arr(col_3)

def check_diag(board):
    diag_1, diag_2 = get_diag(board)
    return check_arr(diag_1) or check_arr(diag_2)

def get_diag(board):
    diag_1 = board[0][0], board[1][1], board[2][2]
    diag_2 = board[0][2], board[1][1], board[2][0]
    return diag_1, diag_2

def check_arr(arr):
    return (len(set(arr)) == 1) and arr[0]

# Display Result
def display_result(board):
    result = check_game_over(board)
    if result == USER_MARKER:
        prompt("User Won")
    elif result == COMPUTER_MARKER:
        prompt("Computer Won")
    else:
        prompt("It's a Tie")

# Pre Load Game Files
ttt_comments_path = get_json_file_path("ttt_comments")
COMMENTS = load_json_file(ttt_comments_path)[PERSONALITY]

# Main Game Loop
introduce_game()
board = initialize_board()

while not(check_game_over(board)):
    display_board(board)
    user_choice = get_user_move(board)
    update_board("user", board, user_choice)

    if (check_game_over(board)):
        break
    computer_choice = get_computer_move(board)
    update_board("computer", board, computer_choice)

display_result(board)