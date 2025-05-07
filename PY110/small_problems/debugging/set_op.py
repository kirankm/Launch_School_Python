data_set = {1, 2, 3, 4, 5}
new_set = set()

for item in data_set:
    if item % 2 == 0:
        new_set.add(item)
data_set -= new_set