lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

lst1[1][-1] = 4
print(lst1)

lst2[-1] = 4
print(lst2)

dict1['first'][-1][-1] = 4
print(dict1)

dict2['a']['a'][-1]
print(dict2)