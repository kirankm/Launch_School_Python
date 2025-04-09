### Program Flow
# Intro
# get the loan amount
    # Validate
    # Comma, _ Removal
# get the interest rate in number : Annual
    # Validate
    # Percentage Removal
# get the Loan Duration in months
    # Validate
    # If Decimal Round Up and give Warning ### Not Done
    # Future Give Option for 3y2m etc ######## Not Done
# Get the Monthly Interest Rate
# Calculate Monthly Payment
# Show Output
# Ask for New Calculation
    # If Yes, clear screen and start agian
    # If No, exit

## Additional Aspects
# Take Comments Out
# Internationalization
# Multiple Random Messages
#XXXXXXXXXX Convert Getting the Continue Question to a separate function
## If Decimal Round Up and give Warning ### Not Done
## Future Give Option for 3y2m etc ######## Not Done


# XXXXXXXXXX Prompt separating output 
# XXXXXXXXXX Deal with no interest loans
# XXXXXXXXXX Show all information (input info) along with  output
# XXXXXXXXXX Rounding outputs
# XXXXXXXXXX Treat for 0 interest rate
# XXXXXXXXXX Deal with the 0 month duration case, while getting the value

# Questions
#### Is there any way, I can avoid multiple calculation, without validation doing multiple tasks
##### One option is to have the validation function return 2 values
#### Is it a good idea to move the warning as a part of the status dictionary?
###############################
# Import Required Libraries
import json
import subprocess
import os

# Settings
DECIMAL_PLACES = 2
LANG = 'en'

# Functions
## General Functions
def prompt(msg, prefix = False):
    if prefix:
        print("\n")
    print(f"==>{msg}")

def load_comments_dict(lang = None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    COMMENTS_FILE_PATH = os.path.join(script_dir, 'mortgage_cal_comments.json')

    with open(COMMENTS_FILE_PATH,'r') as f:
        COMMENTS_FILE = json.load(f)
    if lang is None:
        return COMMENTS_FILE
    return COMMENTS_FILE[lang]

def get_numeric_input(input_name, input_type = "float", chars_to_clean = []):
    while True:
        input_value = input()
        validation_func = get_validation_func(input_type)
        parsing_func = get_parsing_func(input_type)

        cleaned_input_value = clean_input_string(input_value, chars_to_clean)
        input_validation_status = validation_func(cleaned_input_value)

        if input_validation_status is True:
            string_cleaning_warning(cleaned_input_value, input_value)
            return float(cleaned_input_value)
        
        generate_error_prompt(cleaned_input_value, input_validation_status,
                              STATUS_DICT, input_name)

def get_validation_func(input_type):
    if input_type.lower() == "float":
        return validate_float
    return validate_int

def get_parsing_func(input_type):
    if input_type.lower() == "float":
        return float
    return int

def string_cleaning_warning(cleaned_string, original_string):
    if cleaned_string != original_string:
        prompt(COMMENTS['error_messages']['warning_cleaned'])
        prompt(f"{original_string} {COMMENTS['warning_conversion']} {cleaned_string}")

def clean_input_string(input_string, punc_to_remove = [',']):
    for punc in punc_to_remove:
        input_string = input_string.replace(punc, "")
    return input_string

def generate_error_prompt(value, status, status_dict, value_type = "float"):
    msg = status_dict[status].replace("XXXXX", value_type).upper()
    if status == '2':
        prompt(msg)
    else:
        prompt(f"{value} {msg}")

def validate_float(float_str):
    status = False
    try:
        parsed_float = float(float_str)
    except (ValueError, TypeError):
        status = '0'
    else:
        status = check_float_positive(parsed_float)
        if status is True:
            status = check_float_valid(float_str)
    return status

def check_float_valid(float_str):
    invalid_inputs = {'nan', 'inf'}
    if float_str.lower() in invalid_inputs:
        return '1'
    return True

def check_float_positive(parsed_float):
    if parsed_float < 0:
        return '2'
    return True

def validate_int(int_str):
     if int_str.strip().isdigit():
         return True
     return '0'

def clear_screen():
    subprocess.run('clear', shell=True, check = True)

## Introduction
def give_introduction():
    print("\n")
    prompt(COMMENTS['welcome'])
    prompt(COMMENTS['introduction'])
    prompt(COMMENTS['information_prompt'])

## Getting Loan Amount
def get_loan_amount():
    prompt(COMMENTS['loan_amount_prompt'], True)
    return get_numeric_input("loan amount", input_type = "float", 
                             chars_to_clean = [',', "_"])

## Get interest Rate
def get_interest_rate():
    prompt(COMMENTS['interest_rate_prompt'], True)
    return get_numeric_input("interest rate", input_type = "float", 
                             chars_to_clean = ['%'])

## Get Loan Duration
def get_loan_duration():
    prompt(COMMENTS['loan_duration_prompt'], True)
    return get_numeric_input("loan duration", input_type = "int", 
                             chars_to_clean = ['m'])

## Calculate Monthly Installment
def calculate_monthly_installment(amount, annual_interest, duration_in_months):
    monthly_interest = annual_interest / (12 * 100)
    if duration_in_months == 0:
        ## If months 0, Pay the full amount back immediately
        return amount
    elif annual_interest == 0:
        return amount / duration_in_months
    else: 
        return calculate_installment(amount, monthly_interest, 
                                      duration_in_months)
    
def calculate_installment(amount, monthly_interest, duration_in_months):
    numerator = amount * monthly_interest
    denominator = (1 - (1 + monthly_interest)**(-duration_in_months))
    return numerator / denominator

## Display Output
def display_output(original_amount, installment, duration):
    total_amount = installment * max(duration, 1) 
    ### Ensuring that the 0 month case is taken care of
    total_interest = total_amount - original_amount
    prompt(f"{COMMENTS['monthly_installment']} ${round(installment, DECIMAL_PLACES)}", True)
    prompt(f"{COMMENTS['total_amount_paid']} ${round(total_amount, DECIMAL_PLACES)}")
    prompt(f"{COMMENTS['total_interest_paid']} ${round(total_interest, DECIMAL_PLACES)}")

## Should Continue?
def get_continue_confirmation():
    prompt(COMMENTS['continue_prompt'], True)
    while True:
        continue_status =  input().lower()
        if continue_status in ['n', 'no']:
            return False
        elif continue_status in ['y', 'yes']:
            return True
        prompt(COMMENTS['invalid_response'])

# Pre Loading Steps
COMMENTS = load_comments_dict(LANG)

## CONSTANTS
STATUS_DICT = {
    '0':COMMENTS['error_messages']['not_valid'].upper(),
    '1': COMMENTS['error_messages']['not_valid_input'].upper(),
    '2': COMMENTS['error_messages']['only_positive'].upper()
}

# Program Flow
give_introduction()

while True:
    loan_amount = get_loan_amount()
    interest_rate = get_interest_rate()
    loan_duration = get_loan_duration()

    monthly_installment = calculate_monthly_installment(loan_amount, 
                                                interest_rate, loan_duration)

    display_output(loan_amount, monthly_installment, loan_duration)

    should_continue = get_continue_confirmation()
    if not(should_continue):
        break
    clear_screen()

prompt(COMMENTS['exit_message'], True)