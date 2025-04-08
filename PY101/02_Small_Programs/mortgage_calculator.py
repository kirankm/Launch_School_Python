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
    # If Decimal Round Up and give Warning
    # Future Give Option for 3y2m etc
# Get the Monthly Interest Rate
# Calculate Monthly Payment
# Show Output
# Ask for New Calculation
    # If Yes, clear screen and start agian
    # If No, exit

## Additional Aspects
# Take Comments Out
# Prompt separating output
# Internationalization
# Deal with no interest loans
# Show all information (input info) along with  output
# Rounding outputs
# Multiple Random Messages

#### Is there any way, I can avoid multiple calculation, without validation doing multiple tasks
##### One option is to have the validation function return 2 values

#### Is it a good idea to move the warning as a part of the status dictionary?
###############################
# Settings

# CONSTANTS
LOAN_STATUS_DICT = {
    '0':"IS NOT A VALID LOAN AMOUNT",
    '1': "IS NOT A VALID INPUT",
    '2': "Only Positive Values are allowed for Loan Amount!! Try again".upper()
}

# Functions
## General Functions
def prompt(msg):
    print(f"==>{msg}")

## Introduction
def give_introduction():
    prompt("Welcome to the Mortgage Calculator")
    prompt("I will help you figure out your monthly installments")
    prompt("First help me with some information about your loan")

## Getting Loan Amount
def get_loan_amount():
    prompt("What is the total Loan Amount")
    while True:
        loan_amount_input = input()
        cleaned_loan_amount = clean_input_string(loan_amount_input, [',', ""])
        loan_validation_status = validate_loan_amount(cleaned_loan_amount)
        if loan_validation_status is True:
            string_cleaning_warning(cleaned_loan_amount,loan_amount_input)
            return float(cleaned_loan_amount)
        generate_error_prompt(cleaned_loan_amount, loan_validation_status, LOAN_STATUS_DICT)

def validate_loan_amount(loan_amount_str):
    status = False
    try:
        parsed_loan_amount = float(loan_amount_str)
    except (ValueError, TypeError):
        status = '0'
    else:
        status = check_loan_amount_positive(parsed_loan_amount)
        if status is True:
            status = check_loan_amount_valid(loan_amount_str)
    return status

def check_loan_amount_valid(loan_amount_str):
    invalid_inputs = {'nan', 'inf'}
    if loan_amount_str.lower() in invalid_inputs:
        return '1'
    return True

def check_loan_amount_positive(parsed_loan_amount):
    if parsed_loan_amount < 0:
        return '2'
    return True




## Common Functions
def string_cleaning_warning(cleaned_string, original_string):
    if cleaned_string != original_string:
        prompt("WARNING!! THE INPUT STRING WAS CLEANED")
        prompt(f"{original_string} was converted to {cleaned_string}")

def clean_input_string(input_string, punc_to_remove = [',']):
    for punc in punc_to_remove:
        input_string = input_string.replace(punc, "")
    return input_string

def generate_error_prompt(value, status, status_dict):
    if status == '2':
        prompt(status_dict[status])
    else:
        prompt(f"{value} {status_dict[status]}")

# Program Flow
give_introduction()

loan_amount = get_loan_amount()

prompt("What is the Annual Interest Rate")
interest_rate = input()

prompt("What is the loan Duration in months")
loan_duration = input()

monthly_interest_rate = float( interest_rate ) / (12*100)
denominator_part_b = (1 + monthly_interest_rate)**(- float(loan_duration))
denominator = (1 - denominator_part_b)

monthly_installment = float( loan_amount ) * monthly_interest_rate / denominator

prompt(f"The monthly installment amount is {monthly_installment}")