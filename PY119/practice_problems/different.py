'''
Input List
Output number from that list

Questions:
What if empty list, list of size 1,2 and 3
What if 2 items with same count 

D 
Use set for getting unique numbers
for each unique number, get count
if count = 1 return that number, else return the other number
'''


def what_is_different(lst):
    unique_num = list(set(lst))
    return unique_num[0] if lst.count(unique_num[0]) == 1 else unique_num[1]

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)