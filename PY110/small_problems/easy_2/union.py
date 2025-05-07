def union(list1, list2):
    return {*list1, *list2}


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
