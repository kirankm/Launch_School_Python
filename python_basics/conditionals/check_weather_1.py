option_sunny = "It's a beautiful day!"
option_rainy = "Grab your umbrella."
option_else = "Let's stay inside."

weather = "sunny"

match weather:
    case "rainy":
        print(option_rainy)
    case "sunny":
        print(option_sunny)
    case _:
        print(option_else)

