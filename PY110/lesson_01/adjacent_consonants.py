CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = "aeiou"

def sort_by_consonant_count(strings):
    strings.sort(key = count_max_adjacent_consonants, reverse = True)
    return strings

# def sort_key(string):
#     adj_consonants = count_max_adjacent_consonants(string)
#     index_position = strings.index(string)
    
#     return [adj_consonants, len(string) - index_position]

def count_max_adjacent_consonants(string):
    VOWELS = 'aeiou'
    for char in VOWELS:
        string = string.replace(char,"-")
    string_lst = string.split("-")
    sub_str_len_lst = [len(sub_str) for sub_str in string_lst if len(sub_str) > 1]
    return max(sub_str_len_lst, default = 0)


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']