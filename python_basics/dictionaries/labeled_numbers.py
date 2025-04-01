numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

#[print(f'a {key} number is {numbers[key]}') for key in numbers]
[print(f'a {key} number is {value}') for key, value in numbers.items()]