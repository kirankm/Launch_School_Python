"""
P
Input: String
Output: Case Modified Input string

Questions
Empty string to be returned as empty string?

D: Use strings since we can iterate through them
Use list for storing words after splitting them

A:
Split string into words
For every third word, do wierd case transformation
    Else keep original word

wierd case transformation
start with empty string
Iterate through string
If char index is odd keep char as is and append to string
if char index is even, append upper case char
"""

def to_weird_case(text):
    text_lst = text.split()
    text_lst_modified = [weird_case_word(word) if index % 3 == 2 else word 
                         for index, word in enumerate(text_lst)]
    return " ".join(text_lst_modified)

def weird_case_word(word):
    mod_word = ''
    for index, char in enumerate(word):
        new_char = char if index %2 == 0 else char.upper()
        mod_word += new_char 
    return mod_word



#print(weird_case_word("supercalifragilisticexpialidocious") == "sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS")

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)