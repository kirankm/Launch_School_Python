def clean_up(dirty_string):
    clean_string = ''.join(transform_non_alpha(char) for char in dirty_string)
    while '  ' in clean_string:
        clean_string = clean_string.replace("  ", " ")
    return clean_string

def transform_non_alpha(char):
    return char if char.isalpha() else ' '

print(clean_up("---what's my +*& line?") == " what s my line ")