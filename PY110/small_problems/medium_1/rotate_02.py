# Problem
## Input
#number (int)
# count: int: number of last digits to rotate
## Output
# Return the new int with last count digits rotated

## Questions
# What if count is 0
# What if count > string length 

# Explicit Requirements
## The right most count digits of number should be rotated. The left most parts should be left as is
# Implicit requirements
## If count = 1, leave the number as is. 

# Data Structure
## Use strings since they have the option for string slicing

#Algorithm
## Conv number to string
## Extract out last count digits using slicing, keep the remaining parts as suffic

## Code
def rotate_rightmost_digits(num, cnt):
    num_str = str(num)
    left_str = num_str[:-cnt]
    right_str = num_str[-cnt:]
    rotated_right_str = right_str[1:] + right_str[0]
    return int(left_str + rotated_right_str)


## Examples
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True