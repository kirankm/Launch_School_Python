numbers = [1, 2, 3, 4, 5]

def lbyl_6():
    if len(numbers) >= 6:
        return numbers[5]
    return f"There are only {len(numbers)} elements in the list"

def afnp_6():
    try:
        return numbers[5]
    except IndexError:
        return f"There are only {len(numbers)} elements in the list"
    

print(lbyl_6())
print(afnp_6())