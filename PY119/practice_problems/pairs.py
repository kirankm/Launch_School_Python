'''
P
Input List
Out: Int

Explicit
Empty List and List contains only 1 value: -> Return O

Each Number can contribute to only 1 pair [1,1,1] -> Has only 1 pair

Walkthrouhg:
[3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]
3: 2
1: 1
4: 1
5: 3
9: 2
2: 1
6: 1
8: 1
7: 1

One pair of 5,9 and 3 each -> 3


Data Structure
Dictionary for storing counts and values
List for iterating through the original input

Algorithm
For each number: count the number of occurances
Do integer division by 2 to get number of pair each number can form
Sum this to get total number of pairs
'''

def pairs(lst):
    count_dct = {}
    for num in lst:
        count_dct.setdefault(num, 0)
        count_dct[num] += 1
    return sum([cnt // 2 for cnt in count_dct.values()])
    

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
