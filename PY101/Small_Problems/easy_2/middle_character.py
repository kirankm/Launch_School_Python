def center_of(string):
    len_of_string = len(string)
    middle_char = len_of_string // 2
    if len_of_string % 2 == 0:
        return string[middle_char - 1: middle_char+1]
    else:
        return string[middle_char]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True