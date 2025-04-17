def crunch(string):
    if string == "":
        return ''
    curr_val = string[0]
    out_list = [curr_val]
    for val in string:
        if val != curr_val:
            curr_val = val
            out_list.append(val)
    return ''.join(out_list)

def crunch(string):
    curr_val = ''
    out_list = []
    for val in string:
        if val != curr_val:
            curr_val = val
            out_list.append(val)
    return ''.join(out_list)


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')