def repeater(text):
    return "".join([val*2 for val in text])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True


def double_consonants(text):
    vowels = 'aeiou'
    return "".join([char*2 if (char.isalpha() and not(char.lower() in vowels)) else char for char in text ])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")