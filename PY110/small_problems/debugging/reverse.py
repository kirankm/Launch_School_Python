def reverse_string(string):
    new_string = ''
    for char in string:
        new_string = char + new_string

    return new_string

print(reverse_string("hello") == "olleh")