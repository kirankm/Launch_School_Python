numbers = [1, 2, 3, 4, 5] 
new_list = []
for val in numbers[4::-1]:
    new_list.append(val)

test_list = numbers[:]
test_list.reverse()

print(test_list)
print(new_list)
print(numbers)