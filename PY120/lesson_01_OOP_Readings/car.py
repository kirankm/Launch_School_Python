class Car():
    @classmethod
    def get_milage(cls, distance, fuel):
        milage = distance / fuel
        print(f"The milage is {milage}km/ltr")
        return milage

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0
        self.is_engine_on = False

    def turn_engine_on(self):
        if self.is_engine_on:
            print("Engine is already on.")
        else:
            self.is_engine_on = True
            print("Engine is turned on.")

    def turn_engine_off(self):
        self.speed = 0
        if not(self.is_engine_on):
            print("Engine is already off.")
        else:
            self.is_engine_on = False
            print("Engine is turned off.")
    
    def accelerate(self):
        self.speed += 10
        print("Accelerating")
        print(f"Current speed is {self.speed}")

    def brake(self):
        self.speed -= 10
        self.speed = max(0, self.speed)
        print("Braking")
        print(f"Current speed is {self.speed}")


    def get_speed(self):
        print(f"The current speed is {self.speed}")

    def spray_paint_with_color(self, color):
        self.color = color
        print(f"We have spray painted the car with {color}")


    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    def __str__(self):
        return f"{self.model} {self.year} {self.color}"

    def __repr__(self):
        return f"Car({repr(self.model)} {repr(self.year)} {repr(self.color)})"

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

# lumina = Car('chevy lumina', 1997, 'white')
# lumina.get_speed()
# lumina.turn_engine_on()
# lumina.accelerate()
# lumina.accelerate()
# lumina.brake()
# lumina.get_speed()
# lumina.turn_engine_off()

# print(lumina.color)
# lumina.color = "mustard yellow"
# print(lumina.color)

# print(lumina.year)
# print(lumina.model)

# try:
#     lumina.year = 1932
# except AttributeError:
#     print("Unable to set Attribute Model Year")


# lumina.spray_paint_with_color("glowing green")
# print(lumina.color)

# milage = Car.get_milage(500, 40)
# print(f"The car has a milage of {milage} km per ltr")