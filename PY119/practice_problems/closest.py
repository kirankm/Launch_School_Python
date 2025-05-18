"""
P
INput: List : Contains integers
Output: Tuple, size 2, with value in tuple should be there in list as well

Questions
1. What if list size less than 2

Implicit condition:
In tuple first value should be the one appearing first in original list

Walk through
[5, 25, 15, 11, 20]
sorted list would look like
[5, 11, 15, 20, 25]
gap between 5 and 11: 6
11 and 15: 4 


D
Use list, because we can use sorting 

A
created sorted list
Use the sorted list to map each number to the number next to it
    Look for number before and number after and create a dictionary
Iterate through original list
    For each element look in the dictionary and get the gap from closest value
    Keep a track of current_closest gap and element which had that
"""


def closest_numbers(lst):
    sorted_lst = sorted(lst)
    current_sel_number = lst[0]
    current_neighbour = lst[1]
    current_gap = abs(current_sel_number - current_neighbour)
    for val in lst:
        neighbour = closest_neighbour(sorted_lst, sorted_lst.index(val))
        if abs(neighbour - val) < current_gap:
            current_gap = abs(neighbour - val)
            current_sel_number = val
            current_neighbour = neighbour
    return (current_sel_number, current_neighbour) if lst.index(current_sel_number) < lst.index(current_neighbour) else (current_neighbour, current_sel_number)
        

def closest_neighbour(sorted_lst, index):
    number = sorted_lst[index]
    if index == 0:
        closest_neighbor = sorted_lst[index + 1]
    elif index == len(sorted_lst) - 1:
        closest_neighbor = sorted_lst[index - 1]
    else:
        neighbours = sorted_lst[index - 1], sorted_lst[index + 1]
        closest_neighbor = neighbours[1] if abs(number - neighbours[0]) > abs(number - neighbours[1]) else neighbours[0]
    return closest_neighbor

# print(closest_neighbour_gap(sorted([5, 25, 15, 11, 20]), 0))
# print(closest_neighbour_gap(sorted([5, 25, 15, 11, 20]), 1))
# print(closest_neighbour_gap(sorted([5, 25, 15, 11, 20]), 2))
# print(closest_neighbour_gap(sorted([5, 25, 15, 11, 20]), 3))
# print(closest_neighbour_gap(sorted([5, 25, 15, 11, 20]), 4))


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))