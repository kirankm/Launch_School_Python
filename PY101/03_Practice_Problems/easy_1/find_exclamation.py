def find_exclamation(string):
    return string[-1] == "!"

def find_exclamation2(string):
    return string.rfind("!") == len(string) - 1

string1 = "Come over here!"
string2 = "What's up, Doc?"

print(find_exclamation(string1))
print(find_exclamation2(string1))
print(find_exclamation(string2))
print(find_exclamation2(string2))