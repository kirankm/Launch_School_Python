lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def get_odd_sum(lst):
    return sum([val for val in lst if val % 2 == 1])

print(sorted(lst, key = get_odd_sum))