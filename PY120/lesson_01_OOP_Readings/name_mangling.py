class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def speak(self):
        return f"Woof! My name is {self.__name}"
    
    def __dog_years(self):
        return self.__age * 7
    
    def show_age(self):
        print(f"My age in dog_years is {self.__dog_years()}")

sparky = Dog('sparky', 5)

print(sparky.speak())
sparky.show_age()

sparky.__name = "test name"
print(sparky.__name)
print(sparky.speak())

sparky._Dog__name = "Joe"
print(sparky.__name)
print(sparky.speak())