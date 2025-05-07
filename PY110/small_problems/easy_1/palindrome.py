"""PEDAC
Questions: 
1. Does case matter : Yes
2. How does punctuations and space affect: Punctuations and space also should be palindromatic
"""
def is_real_palindrome(string):
    clean_str = cleaned_string(string)
    return is_palindrome(clean_str)

def cleaned_string(string):
    temp_str = string.casefold()
    clean_str = ""
    for char in temp_str:
        if char.isalnum():
            clean_str += char
    return clean_str

def is_palindrome(string):
    return string == string[::-1]


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True