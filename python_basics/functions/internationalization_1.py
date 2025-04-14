def greet(lang):
    match lang:
        case "en":
            print("Hi!")
        case "fr":
            print("Salut!")
        case _:
            print("_")

greet("en")
