import subprocess
import shutil
import json
import time

def prompt(msg, prefix_space = False):
    if prefix_space:
        print("\n")
    if isinstance(msg, list):
        msg = "\n".join(msg)
    print(f"==> {msg}")

def clear_screen(msg = None):
    subprocess.run('clear', shell=True, check = True)
    if msg:
        display_banner(msg)

def load_json_file(json_file_path):
    with open(json_file_path,'r') as f:
        loaded_file = json.load(f)
    return loaded_file

def get_user_input(prompt_msg, error_msg, choices, process_choice = str.lower):
    prompt(prompt_msg, prefix_space= True)
    while True:
        usr_choice = input()
        if process_choice:
            usr_choice = process_choice(usr_choice)
        if callable(choices):
            if check_choice_validity_function(usr_choice, choices):
                return usr_choice
        else:
            if check_choice_validity(usr_choice, choices):
                return usr_choice
        prompt(error_msg, prefix_space= True)
    

def check_choice_validity_function(choice, valid_fn):
    return valid_fn(choice)

def check_choice_validity(choice, choices):
    if choice in choices:
        return True
    if isinstance(choices, dict):
        if choice in choices.values():
            return True
    return False

def display_banner(message):
    banner_width = shutil.get_terminal_size().columns
    msg = message.upper()

    line1 = "*" * banner_width
    line2 = f"*{' '*(banner_width - 2)}*"
    line3 = f"*{msg.center(banner_width - 2)}*"
    banner = [line1, line2, line3, line2, line1]

    print("\n".join(banner))

def replace_last(text, old, new):
    parts = text.rsplit(old, 1)
    return new.join(parts) if len(parts) == 2 else text


def wave_hands_bye(game_name):
    ANIMATION_CYCLES = 5
    ANIMATION_FRAME_DELAY = .2
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


    for _ in range(ANIMATION_CYCLES):
        for frame in frames:
            clear_screen()
            prompt(f"Thanks for playing {game_name}")
            print(frame)
            time.sleep(ANIMATION_FRAME_DELAY)