class Pet():
    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f"Hi, I am {self.name}. I am {type_name}")

class Dog(Pet):
    def speak(self):
        print(f"{self.name} says Woof!")

class cat(Pet):
    def speak(self):
        print(f"{self.name} says Meow!")

class Parrot(Pet):
    def speak(self):
        print(f"{self.name} wants a cracker!")

sparky = Dog("Sparky")
#sparky.speak()

fluffy = cat("fluffy")
#sparky.speak()

polly = Parrot("Polly")
#sparky.speak()

for pet in [sparky, fluffy, polly]:
    pet.speak()