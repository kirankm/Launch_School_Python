## Iterate through the string
## Keep track of a counter
## If counter becomes negative or final value is not 0 return false


def is_balanced(string):
    pending_para = 0
    for el in string:
        if el == "(":
            pending_para += 1
        elif el == ")":
            pending_para -= 1
        if pending_para < 0:
            break
    return pending_para == 0

def is_balanced_all(string, open_char, close_char):
    balance_cnt = 0
    for el in string:
        if el == open_char:
            balance_cnt += 1
        elif el == close_char:
            balance_cnt -= 1
        if balance_cnt < 0:
            break
    return balance_cnt == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True