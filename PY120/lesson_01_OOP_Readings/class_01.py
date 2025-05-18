class GoodDog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        type_name = type(self).__name__
        print(type_name)
        print(f"Constructor for {self.name}")

    def speak(self):
        print(f"Woof! I am {self.name}. I am {self.age} years old")

    def rollover(self):
        print(f"{self.name} is rolling over")

spark = GoodDog("sparky", 5)
spark.speak()
spark.rollover()

rover = GoodDog("rover", 10)
rover.speak()
rover.rollover()

print(spark)
print(rover)

