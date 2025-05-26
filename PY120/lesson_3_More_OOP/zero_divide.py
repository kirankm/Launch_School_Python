def get_number(num_name):
    num_str = input(f"Give {num_name} number: ")
    try:
        num = float(num_str)
    except ValueError:
        print("Only Numeric Values are allowed")
        raise ValueError
    return num




try:
    num_01 = get_number("first")
    num_02 = get_number("second")
    result = num_01 / num_02
except (ZeroDivisionError, ValueError) as e:
    print(e)
else:
    print(f"The result is {result}")
finally:
    print("End of the program")