### PEDAC
### Understand problem
## Inputs
# ideally List, can be non list also
## Output
# If list with len > 1, return rotated list
# if list len = 1 return same list
# If not a list return None
# Should be a new list

### Algorithm
## ifnot a list return none, if empty list return empty list
## for others taken the elements from index 1 to last and append a list with just first element to it's end

#Code

def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    if not lst:
        return lst
    return lst[1:] + [lst[0]]

# All of these examples should print True
## Example Questions
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])