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
# Functions

## Introduction
def introduce():
    print("Welcome to the Calculator\n"
      "I can Add, Subtract, Multiply, Divide")

## Dealing With Numbers
def get_number(number_type = None):
    num_str = get_number_input(number_type)
    clean_num = clean_num_str(num_str)
    verified_num = verify_num(clean_num)
    if verified_num:
        final_num = process_number(verified_num)
    return verified_num and final_num

def get_number_input(number_type):
    if number_type is None:
        comment = "Give me a Number: "
    else:
        comment = f"Give me the {number_type} number: "
    return input(comment)

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

def verify_num(num_str):
    return num_str.isdigit() and num_str

## Dealing With Operator
def get_operator_input():
    comment = '''What operation would you like to perform?\n
                1) Add 2) Subtract 3) Multiply 4) Divide: '''
    return input(comment)

def get_operation(operator, operator_dict):
    for val in OPERATOR_DICT:
        if operator in val:
            return operator_dict[val]

## Different Operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# Variables
OPERATOR_DICT = {
    '1) Add': add,
    '2) Subtract' : subtract,
    '3) Multiply' : multiply,
    '4) Divide': divide
}


###############################
# Program Flow
introduce()
first = get_number("first")
second = get_number("second")
operator = get_operator_input()
operation =get_operation(operator, OPERATOR_DICT)
result = operation(first, second)


# print(f'The numbers are {first}, {second}')
# print(f'The operator is {operator}')
# print(f'The operation is {operation}')

print(f'The result is {result}')
