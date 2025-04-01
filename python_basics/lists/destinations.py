destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(val, arr):
    for element in destinations:
        if val == element:
            return True
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # True
