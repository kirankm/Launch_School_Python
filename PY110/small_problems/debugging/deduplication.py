data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
seen = set()
unique_lst = []
for num in data:
    if num not in seen:
        unique_lst.append(num)
        seen.add(num)

print(unique_lst)


data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
unique_data.sort(key = lambda x:data.index(x))
print(unique_data)