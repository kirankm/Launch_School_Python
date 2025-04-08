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
    



# Program Flow
give_introduction()

prompt("What is the total Loan Amount")
loan_amount = input()

prompt("What is the Annual Interest Rate")
interest_rate = input()

prompt("What is the loan Duration in months")
loan_duration = input()

monthly_interest_rate = float( interest_rate ) / (12*100)
denominator_part_b = (1 + monthly_interest_rate)**(- float(loan_duration))
denominator = (1 - denominator_part_b)

monthly_installment = float( loan_amount ) * monthly_interest_rate / denominator

prompt(f"The monthly installment amount is {monthly_installment}")

