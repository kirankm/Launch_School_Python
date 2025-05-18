'''
Question: Only Lower case?


'''

def longest_vowel_substring(text):
    VOWEL = 'aeiou'
    char_to_replace = set([char for char in text if char not in VOWEL])
    new_text = text[:]
    for char in char_to_replace:
        new_text = new_text.replace(char, '-')
    new_text_list = new_text.split("-")
    return max([len(sub_str) for sub_str in new_text_list])


print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)