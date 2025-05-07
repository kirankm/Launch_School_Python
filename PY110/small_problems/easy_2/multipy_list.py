def multiply_list(list1, list2):
    return [list1[i] * list2[i] for i in range(len(list1))]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True