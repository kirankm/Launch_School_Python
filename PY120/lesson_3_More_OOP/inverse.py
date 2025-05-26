def get_inverse(num_list):
    return [get_inverse_num(num) for num in num_list]


def get_inverse_num(num):
    try:
        value = 1 / num
    except TypeError:
        print("Only numbers are allowed")
    except ZeroDivisionError:
        print("0 is not a permissible value")
        return float('inf')
    else:
        return value
    


print(get_inverse([1,2,3, 0]))

print(get_inverse([1,2,3, 'a']))

print(get_inverse([1,2,3, 'a', 0]))

print(get_inverse([1,2,3]))