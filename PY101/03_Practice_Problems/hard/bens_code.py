def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    return True


ip1 = "10.4.5.11"
ip2 = "4.5.5"
ip3 = "1.2.3.4.5"
print(is_dot_separated_ip_address(ip1))
print(is_dot_separated_ip_address(ip2))
print(is_dot_separated_ip_address(ip3))