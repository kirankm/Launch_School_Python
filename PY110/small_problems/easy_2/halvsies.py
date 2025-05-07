import math

def halvsies(lst):
    mid_point = math.ceil(len(lst) / 2)
    return [lst[:mid_point], lst[mid_point:]]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])