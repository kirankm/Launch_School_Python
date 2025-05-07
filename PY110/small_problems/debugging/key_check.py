def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))