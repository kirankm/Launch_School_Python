'''
P
Input: String
Output: Dictionary: Key char, value count
Only lower case letters in the original string

Empty String: Empty Dict
No alphabets: Empty Dict

filter: Only lower case letters

Question:
If a letter is both upper and lower, should only lower be considered?

D: Dictionary for storin count as value and letter as key
String: is good enough for iterating through

A
Iterate through the string
If lower case letter, increment count

Or using comprehension
'''


def count_letters(text):
    return {char: text.count(char) for char in text if char.isalpha() and (char.lower() == char)}

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})