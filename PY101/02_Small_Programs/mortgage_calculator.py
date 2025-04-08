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

###############################
# Settings

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
        cleaned_loan_amount = clean_loan_amount(loan_amount_input)
        if is_valid_loan_amount(cleaned_loan_amount):
            string_cleaning_warning(cleaned_loan_amount,loan_amount_input)
            return float(cleaned_loan_amount)

def clean_loan_amount(loan_amount_str):
    punc_to_remove = [',', '_']
    for punc in punc_to_remove:
        loan_amount_str = loan_amount_str.replace(punc, "")
    return loan_amount_str

def is_valid_loan_amount(loan_amount_str):
    status = False
    try:
        parsed_loan_amount = float(loan_amount_str)
    except (ValueError, TypeError):
        prompt("Hmm.. the Loan Amount Doesn't look valid!! Try Again")
    else:
        status = check_loan_amount_positive(parsed_loan_amount)
        if status:
            status = check_loan_amount_valid(loan_amount_str)
    return status

def check_loan_amount_valid(loan_amount_str):
    invalid_inputs = {'nan', 'inf'}
    if loan_amount_str in invalid_inputs:
        prompt(f"{loan_amount_str} is not a valid input")
        return False
    return True

def check_loan_amount_positive(parsed_loan_amount):
    if parsed_loan_amount < 0:
        prompt("Only Positive Values are allowed for Loan Amount!! Try again")
        return False
    return True

## Common Functions
def string_cleaning_warning(cleaned_string, original_string):
    if cleaned_string != original_string:
        prompt("WARNING!! THE INPUT STRING WAS CLEANED")
        prompt(f"{original_string} was converted to {cleaned_string}")

#def clean_input_string(input_string, punc_to_remove = [',', ""])


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