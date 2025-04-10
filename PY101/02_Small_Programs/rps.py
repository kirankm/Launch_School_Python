## Flow
# Give Intro Screen
    # Help, New Game, Settings, Past Performance
# Give Current Game Stat (Round Robin, How Many Done)
# Get User Input
# Generate Computer Input
# Compare User vs Computer and Get Result
# Declare Result
    # Show What User did, Computer Did, Result
# Ask if We should Play Again



# Additional Aspects
## Create Game History
## Create Best Performance

######
# Import Libraries
import json
import os
import types


# Common Functions
def prompt(msg, prefix_space = False):
    if prefix_space:
        print("\n")
    if isinstance(msg, list):
        msg = "\n".join(msg)
    print(f"==> {msg}")

def get_valid_input(prompt_msg, error_msg, valid_input):
    prompt(prompt_msg, True)
    while True:
        user_input = input().strip().lower()

        if isinstance(valid_input, types.FunctionType):
            validation_status = valid_input(user_input)
        else:
            validation_status = user_input in [
                x.lower() for x in valid_input
                ]

        if validation_status:
            return user_input
        prompt(error_msg)

# Pre Load Game Functions
def load_rps_files(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, file_name)

    with open(json_file_path,'r') as f:
        json_file = json.load(f)
    return json_file

# Introduction
def introduce():
    intro_msg = RPS_COMMENTS['intro']
    intro_error_msg = RPS_COMMENTS['intro_error']
    valid_input = ['h', 'c', 'n', 's']
    user_choice = get_valid_input(intro_msg, intro_error_msg, valid_input)
    return user_choice

# Pre Load Game Files
RPS_SETTINGS = load_rps_files("rps_config.json")
PERSONALITY = RPS_SETTINGS['personality']

RPS_COMMENTS = load_rps_files("rps_comments.json")[PERSONALITY]



# Program Flow
introduce()