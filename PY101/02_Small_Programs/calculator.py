# Import Statements
import subprocess
import json
import os

# Settings
LANG = 'en'
DECIMAL_PLACES =  3

# Functions

## Common Functions
def prompt(message):
    print(f"==> {message}")

def clear_screen():
    subprocess.run('clear', shell=True, check = True)

## Introduction
def introduce():
    prompt(COMMENTS['welcome'])
    prompt(COMMENTS['capabilities'])

## Dealing With Numbers
def get_number(number_type = None):
    while True:
        num_str = get_number_input(number_type)
        cleaned_num_str = clean_num_str(num_str)
        valid_num_str = is_num_str(cleaned_num_str)
        if valid_num_str:
            if cleaned_num_str != num_str:
                prompt(COMMENTS['punctuation_warning'])
            return process_number(valid_num_str)
        prompt(COMMENTS['invalid_number'])

def get_number_input(number_type):
    if number_type is None:
        comment = COMMENTS["generic_number_prompt"]
    else:
        comment = COMMENTS[f'{number_type}_number_prompt']
    prompt(comment)
    return input()

def process_number(num_str):
    return float(num_str)

def clean_num_str(num_str):
    temp_str = remove_punc(num_str)
    return temp_str

def remove_punc(num_str):
    punc_rem = [',', '-', '_']
    for punc in punc_rem:
        num_str = num_str.replace(punc,'')
    return num_str

def is_num_str(num_str):
    is_potential_decimal = num_str.count(".") <= 1
    is_numeric = False
    if is_potential_decimal:
        mod_num_str = num_str.replace(".","")
        is_numeric = mod_num_str.isdigit()
    return is_potential_decimal and is_numeric and num_str

## Dealing With Operator
def get_operation():
    comment = COMMENTS['operation_prompt']
    prompt(comment)
    while True:
        operation_input = input()
        if operation_input in OPERATOR_DICT:
            return operation_input
        prompt(COMMENTS['invalid_operation'])

def get_operation_func(operator, operator_dict):
    return operator_dict.get(operator, None)

## Different Operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        prompt(COMMENTS['division_by_zero'])
        return None
    return a / b

## Display Output
def display_output(answer, decimal_places = DECIMAL_PLACES):
    if result:
        prompt(f'{COMMENTS['result']} {round(answer, decimal_places)}')

## Should Continue?
def get_continue_confirmation():
    prompt(COMMENTS["continue_prompt"])
    return input()

# Variables
OPERATOR_DICT = {
    '1': add,
    '2' : subtract,
    '3' : multiply,
    '4': divide
}

# Load Comments
script_dir = os.path.dirname(os.path.abspath(__file__))
COMMENTS_FILE_PATH = os.path.join(script_dir, 'calc_comments.json')

with open(COMMENTS_FILE_PATH,'r') as f:
    COMMENTS_FILE = json.load(f)

COMMENTS = COMMENTS_FILE[LANG]
###############################
# Program Flow
introduce()
while True:
    first = get_number("first")
    second = get_number("second")

    operation = get_operation()
    operation_func =get_operation_func(operation, OPERATOR_DICT)

    result = operation_func(first, second)

    display_output(result, DECIMAL_PLACES)

    should_continue = get_continue_confirmation()
    if should_continue.lower() in ['n', 'no']:
        break
    clear_screen()

prompt(COMMENTS['exit_message'])
