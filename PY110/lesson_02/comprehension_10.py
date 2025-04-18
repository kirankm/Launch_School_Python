from random import choice

def apply_choice(options, count):
    return ''.join(choice(options) for _ in range(count))

def create_uuid():
    options = '0123456789abcdef'
    pattern = [8, 4, 4, 4, 12]
    return '-'.join([apply_choice(options, val) for val in pattern])

print(create_uuid())
print(create_uuid())
print(create_uuid())

