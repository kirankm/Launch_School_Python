def is_empty_or_blank(string):
    return len(string.replace(" ","")) == 0

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True