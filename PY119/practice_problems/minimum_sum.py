"""
P
Input : list 
Output: Int or None

Walkthrough
Input: [55, 2, 6, 5, 1, 2, 9, 3, 5, 100]
if we start at index 0, sum is high
at index 1: 2+6+5+1+2 : 16
index 2 is higher 
index 3: Higher


Question:
Should I worry about input not being a list, 
Should I worry about numbers being non integers: Doesnt' matter
Ties

D: Use lists, since slicing and iterating in order are important

A:
Start at the top of the list:
Get a list of size 5 starting from the start point
Sum the list
Increment starting point by 1
"""
def minimum_sum(lst):
    if len(lst) < 5: 
        return None
    current_min_sum = float('inf')
    for i in range(len(lst) - 4):
        new_sum = sum(lst[i:i+5])
        if current_min_sum > new_sum:
            current_min_sum = new_sum
    return current_min_sum



print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)