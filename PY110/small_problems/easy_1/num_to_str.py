DIGIT_STR_MAP = {num:str(num) for num in range(0, 10)}

def signed_integer_to_string(number):
    if number:
        sign = "+" if number > 0 else "-"
        return sign + integer_to_string(abs(number))
    return "0"

def integer_to_string(number):
    remainder = number
    string = ""
    while remainder > 0:
        new_digit = remainder % 10
        string = DIGIT_STR_MAP[new_digit] + string
        remainder = (remainder - new_digit) // 10

    return "0" if string == "" else string


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True