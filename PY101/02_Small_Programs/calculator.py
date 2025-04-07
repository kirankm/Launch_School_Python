################
#  X Introduction
# X Get First Number
    # Process First Number
# X Get Second Number
    # Process Second Number
# Get Operation
    # Process Operation
# Perform Calculation
# Display Result

#################
# Import Statements
import subprocess

# Functions

## Common Functions
def prompt(message):
    print(f"==> {message}")

def clear_screen():
    subprocess.run('clear', shell=True)

## Introduction
def introduce():
    prompt("Welcome to the Calculator")
    prompt("I can Add, Subtract, Multiply, Divide\n")

## Dealing With Numbers
def get_number(number_type = None):
    while True:
        num_str = get_number_input(number_type)
        cleaned_num_str = clean_num_str(num_str)
        valid_num_str = is_num_str(cleaned_num_str)
        if valid_num_str:
            if cleaned_num_str != num_str:
                prompt("WARNING!!! REMOVING PUNCTUATIONS FROM INPUT\n")
            return process_number(valid_num_str)
        prompt("Hmm... that doesn't look like a valid number.\n")

def get_number_input(number_type):
    if number_type is None:
        comment = "Give me a Number: "
    else:
        comment = f"Give me the {number_type} number: "
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
    return num_str.isdigit() and num_str

## Dealing With Operator
def get_operation():
    comment = 'What operation would you like to perform?\n\
    1) Add 2) Subtract 3) Multiply 4) Divide: '
    prompt(comment)
    while True:
        operation_input = input()
        if operation_input in OPERATOR_DICT:
            return operation_input
        prompt("You must choose 1, 2, 3, or 4")

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
        prompt("Cannot Do Division with 0")
        return None
    return a / b

## Should Continue?
def get_continue_confirmation():
    prompt("Do you want to continue? Say Yes(y) or No(n)")
    return input()

# Variables
OPERATOR_DICT = {
    '1': add,
    '2' : subtract,
    '3' : multiply,
    '4': divide
}


###############################
# Program Flow
introduce()
while True:
    first = get_number("first")
    second = get_number("second")

    operation = get_operation()
    operation_func =get_operation_func(operation, OPERATOR_DICT)

    result = operation_func(first, second)

    prompt(f'The result is {result}')

    should_continue = get_continue_confirmation()
    if should_continue.lower() in ['n', 'no']:
        break
    else:
        clear_screen()

prompt("Exiting the Calculator. Until we meet again!!")
