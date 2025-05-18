'''
P
Input: String (but the value inside is an integer)
Output: Number (integer) of even substrings

Explicit
If sub string repeats, both should be counted

Questions

1. Should we check if it's an integer or are floats also allowed

D:
Nested list for storing all substrings

A
Create a list of all substrings of the original num string
For each substring check if the value is even
Return total count


Create all sub string

sub_str_lst = []
Start Length = 1
Start Index = 0

Iterate through string and append to sub_str_lst, by changing start index
    
Once finished iterating Increment Length by 1, set start index to 0
Inc
'''

def even_substrings(num_str):
    sub_str_lst = list_all_substrings(num_str)
    return len([num for num in sub_str_lst if int(num) % 2 == 0])

def list_all_substrings(text):
    sub_str_lst = []
    for str_len in range(1, len(text) + 1):
        for start_index in range(len(text) - str_len + 1):
            sub_str_lst.append(text[start_index: start_index + str_len])
    return sub_str_lst


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)