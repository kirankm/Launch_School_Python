lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

out_list = [sorted(x, key = str) for x in lst]
print(out_list)