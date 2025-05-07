def swap(string):
    return " ".join([swap_word(word) for word in string.split(" ")])

def swap_word(word):
    return f"{word[-1]}{word[1:-1]}{word[0]}" if len(word) > 1 else word


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True