'''
P
Input : String
Output: Character (string of length 1)

Explicit
Case doesnt matter
Return lower case character
Return first character


Questions
What to do with empty string


D: String and I can iterate through it
Dictionary for tracking count

A:
Convert string to lower case
Create a dictionary with char and count 
If seen already increase count by 1
'''

def most_common_char(text):
    text = text.lower()
    count_dict = {}
    curr_max = 0
    for char in text:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1
        if count_dict[char] > curr_max:
            curr_max = count_dict[char]
    common_chars = [key for key in count_dict if count_dict[key] == curr_max]
    common_chars.sort(key = lambda x:text.index(x))
    return common_chars[0]


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')