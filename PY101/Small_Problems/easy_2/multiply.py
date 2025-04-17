def multiply(a,b):
    return a * b

#print(multiply(5, 3) == 15) 

def square(a):
    return multiply(a,a)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

def power(val, n):
    result = 1
    for _ in range(n):
        result = multiply(result, val)
    return result

print(power(5,2) == 25)   # True
print(power(-8, 3) == -512)  # True