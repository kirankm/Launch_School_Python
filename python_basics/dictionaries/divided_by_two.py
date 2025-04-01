numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = [int(val/2) for val in numbers.values()]
print(half_numbers)