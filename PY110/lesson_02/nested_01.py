lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

print(lst1[-1][-1][-1])
print(lst2[-1]['third'][0])
print(lst3[-1]['third'][0][0])
print(dict1['b'][-1])
print(list(dict2['3rd'].keys())[0])