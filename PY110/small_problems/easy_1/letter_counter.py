def word_sizes(string):
    word_len_lst = [get_alphabet_len(word) for word in string.split()]
    return {word_len:word_len_lst.count(word_len) for word_len in set(word_len_lst)}

def get_alphabet_len(word):
    return len([char for char in list(word) if char.isalpha()])


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})