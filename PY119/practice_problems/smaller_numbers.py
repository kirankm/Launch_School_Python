"""
P 
input: list
Output: same length list
Questions:
1. What if empty list

Explicit Conditions 
Implicit Conditions 

Walkthrough with an example
[8, 1, 2, 2, 3]
There are 3 unique numbers less than 8: 
There are 0 unique numbers less than 1
There is 1 unique number less than 2
There are 2 unique numbers less than 3

If we sort the unique numbers in original list:
    It will give [1,2 3, 8]
    Looks like the indices corresponding to the numbers are the required values
D : Use set for de duplication, since we want unique numbers, use lists since we might need sorting and indexing
A : 
Get list with unique numbers
sort the list
For each number in original list, return the index
"""



def smaller_numbers_than_current(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return [unique_lst.index(num) for num in lst]

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)