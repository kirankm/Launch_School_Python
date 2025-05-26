class Car:
    manufacturer = "BMW"
    def __init__(self):
        self.manufacturer = 'Mercedes'

    def show_manufacturer(self):
        print(f"{self.__class__.manufacturer=}")
        print(f"{self.manufacturer=}")
    
a = Car()
a.show_manufacturer()