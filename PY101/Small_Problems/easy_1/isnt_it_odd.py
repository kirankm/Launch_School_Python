def is_odd(integer):
    abs_val = abs(integer)
    return abs_val % 2 == 1

print(is_odd(3))
print(is_odd(4))
print(is_odd(0))
print(is_odd(-1))
print(is_odd(-3))
