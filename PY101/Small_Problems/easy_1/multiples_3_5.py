def multisum(val):
    return sum([x for x in range(1, val + 1) if x % 3 == 0 or x % 5 == 0])

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)