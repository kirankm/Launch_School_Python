def repeated_substring(text):
    text_length = len(text)
    for sub_str_len in range(1, text_length + 1):
        if text_length % sub_str_len != 0:
            continue
        multiplier = text_length // sub_str_len
        if text[:sub_str_len] * multiplier == text:
            return (text[:sub_str_len], multiplier)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))