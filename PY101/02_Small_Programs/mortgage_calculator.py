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
# XXXXXXXXXX Prompt separating output 
# Internationalization
# XXXXXXXXXX Deal with no interest loans
# XXXXXXXXXX Show all information (input info) along with  output
# Rounding outputs
# Multiple Random Messages
# Convert Getting the Continue Question to a separate function
# XXXXXXXXXX Treat for 0 interest rate
# Deal with the 0 month duration case, while getting the value

#### Is there any way, I can avoid multiple calculation, without validation doing multiple tasks
##### One option is to have the validation function return 2 values

#### Is it a good idea to move the warning as a part of the status dictionary?
### Should I move getting numbers as a generic function
###############################
import subprocess

# Settings
DECIMAL_PLACES = 2

# CONSTANTS
STATUS_DICT = {
    '0':"IS NOT A VALID XXXXX",
    '1': "IS NOT A VALID INPUT FOR XXXXX",
    '2': "Only Positive Values are allowed for XXXXX!! Try again".upper()
}

# Functions
## General Functions
def prompt(msg, prefix = False):
    if prefix:
        print("\n")
    print(f"==>{msg}")

## Introduction
def give_introduction():
    print("\n")
    prompt("Welcome to the Mortgage Calculator")
    prompt("I will help you figure out your monthly installments\n")
    prompt("First help me with some information about your loan\n")

## Getting Loan Amount
def get_loan_amount():
    prompt("What is the total Loan Amount")
    while True:
        loan_amount_input = input()
        cleaned_loan_amount = clean_input_string(loan_amount_input, [',', "_"])
        loan_validation_status = validate_float(cleaned_loan_amount)
        if loan_validation_status is True:
            string_cleaning_warning(cleaned_loan_amount,loan_amount_input)
            return float(cleaned_loan_amount)
        generate_error_prompt(cleaned_loan_amount, 
                              loan_validation_status, STATUS_DICT,
                              'loan amount')

## Get interest Rate
def get_interest_rate():
    prompt("What is the Annual Interest Rate", True)
    while True:
        interest_rate_input = input()
        cleaned_interest_rate = clean_input_string(interest_rate_input, ['%'])
        interest_validation_status = validate_float(cleaned_interest_rate)
        if interest_validation_status is True:
            return float(cleaned_interest_rate)
        generate_error_prompt(cleaned_interest_rate, 
                              interest_validation_status, STATUS_DICT,
                              'interest rate')

## Get Loan Duration
def get_loan_duration():
    prompt("What is the Duration of the loan", True)
    while True:
        loan_duration_input = input()
        cleaned_loan_duration = clean_input_string(loan_duration_input, ['m'])
        duration_validation_status = validate_int(cleaned_loan_duration)
        if duration_validation_status is True:
            return float(cleaned_loan_duration)
        generate_error_prompt(cleaned_loan_duration, 
                              duration_validation_status, STATUS_DICT,
                              'loan duration')


## Calculate Monthly Installment
def get_monthly_installment(amount, annual_interest, duration_in_months):
    monthly_interest = annual_interest / (12 * 100)
    if duration_in_months == 0:
        ## If months 0, pay with 1 month interest
        return amount * (1 + monthly_interest)
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
    prompt(f"The monthly installment is {installment}", True)
    prompt(f"The total Amount Paid is, {total_amount}")
    prompt(f"The total interest paid is {total_interest}")

## Should Continue?
def get_continue_confirmation():
    prompt("Would you like to Calculate the Installment Again", True)
    return input()

## Common Functions
def string_cleaning_warning(cleaned_string, original_string):
    if cleaned_string != original_string:
        prompt("WARNING!! THE INPUT STRING WAS CLEANED")
        prompt(f"{original_string} was converted to {cleaned_string}")

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

# Program Flow
give_introduction()

while True:
    loan_amount = get_loan_amount()
    interest_rate = get_interest_rate()
    loan_duration = get_loan_duration()

    monthly_installment = get_monthly_installment(loan_amount, 
                                                interest_rate, loan_duration)

    display_output(loan_amount, monthly_installment, loan_duration)

    should_continue = get_continue_confirmation()
    if should_continue.lower() in ['n', 'no']:
        break
    clear_screen()

prompt("Until We see again", True)