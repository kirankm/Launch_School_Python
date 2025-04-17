def greet_user():
    name = input("Tell me your name: ")
    # if name.endswith("!"):
    #     greeting = "HELLO {name} WHY ARE WE YELLING?".upper()
    # else:
    #     greeting = "Hello {name}"
    greeting = f"HELLO {name} WHY ARE WE YELLING?".upper() if name.endswith("!") else f"Hello {name}."
    print(greeting)
        
greet_user()