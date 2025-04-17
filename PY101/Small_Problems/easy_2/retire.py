from datetime import datetime

age = int(input("What is your age?: \n"))
retirement_age = int(input("What is your preferred retirement age?: \n"))

current_year = datetime.now().year
years_till_retirement = retirement_age - age
year_of_retirement = current_year + years_till_retirement

print(f"It's {current_year}. You will retire in {year_of_retirement}.")
print(f"You have only {years_till_retirement} years of work to go!")
