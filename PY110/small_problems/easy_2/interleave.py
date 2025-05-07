def interleave(lst_1, lst_2):
    zipped_list = zip(lst_1, lst_2)
    return [item for sublist in zipped_list for item in sublist]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)   