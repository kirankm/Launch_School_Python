def get_number_from_user(nth):
    msg = f"Enter the {nth} number: "
    return input(msg)

def get_num_with_suffix(num):
    match num:
        case 1:
            return '1st'
        case 2:
            return '2nd'
        case 3:
            return '3rd'
        case _:
            return f'{num}th'
        

def search_101():
    num_array = [get_number_from_user(get_num_with_suffix(num)) for num in range(1,7)]
    verb = 'is' if  num_array[-1] in num_array[:-1] else "isn't"
    print(f"{num_array[-1]} {verb} in {",".join(num_array[:-1])}.")

search_101()
