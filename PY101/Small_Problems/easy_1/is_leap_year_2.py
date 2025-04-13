def is_leap_year_georgian(year):
    div_by_400 = year % 400 == 0
    div_by_100 = year % 100 == 0
    div_by_4 = year % 4 == 0
    return ((div_by_400) or (div_by_4 and not(div_by_100)))

def is_leap_year_julian(year):
   return year % 4 == 0

def is_leap_year(year):
    return is_leap_year_georgian(year) if year >= 1752 else year % 4 == 0

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)