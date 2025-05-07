def string_to_signed_integer(string):
    sign = -1 if string[0] == "-" else 1
    return conv_to_int(string) if string[0].isdigit() else sign * conv_to_int(string[1:])

def conv_to_int(string):
    return sum([(10 ** (len(string) - index - 1)) * conv_to_int_digit(char) for index, char in enumerate(string)])

def conv_to_int_digit(string):
    string_int_map = {str(num):num for num in range(0,10)}
    return string_int_map[string]

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
