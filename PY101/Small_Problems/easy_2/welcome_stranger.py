def greetings(name_list, role_dict):
    name = " ".join(name_list).title()
    role = " ".join(role_dict.values()).title()
    return  f"Hello, {name}! Nice to have a {role} around."

def greetings(name_list, role_dict):
    return  f"Hello, {" ".join(name_list)}! Nice to have a {" ".join(role_dict.values())} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)