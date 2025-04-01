def first(arr):
    if not isinstance(arr, list):
        print("Warning! Provided input is not a List")
    elif len(arr) == 0:
        print("Warning! No element in the provided List")
    else:
        return arr[0]

print(first('e'))
print(first(['Earth', 'Moon', 'Mars']))