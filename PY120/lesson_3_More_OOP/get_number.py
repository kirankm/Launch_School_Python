class NegativeNumberError(ValueError):
    def __init__(self, msg = "Negative Values are not allowed"):
        super().__init__(msg)

num = input("Give me a positive number")

try:
    float(num)
except:
    raise TypeError("Only numbers are allowed")

if float(num) < 0:
    raise NegativeNumberError

print(f"The number you have given is {num}")