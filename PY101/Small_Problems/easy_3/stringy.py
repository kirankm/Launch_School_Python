def stringy(length):
    val = 1
    out_list = []
    for i in range(length):
        out_list.append(val)
        val = int(not(val))
    return ''.join([str(x) for x in out_list])

def string(length):
    return ''.join([str(i%2) for i in range(1, length + 1)])


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True