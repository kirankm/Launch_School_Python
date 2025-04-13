def short_long_short(str_1, str_2):
    return str_1 + str_2 + str_1 if len(str_1) < len(str_2) else str_2 + str_1 + str_2

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")