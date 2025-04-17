def penultimate(string):
    return string.split(" ").pop(-2)

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def get_middle_word(string):
    string_array = string.split(" ")
    pop_index = 0
    while len(string_array) > 1:
        string_array.pop(pop_index)
        pop_index = 0 if pop_index != 0 else -1
    return string_array[0]