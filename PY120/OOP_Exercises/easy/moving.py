class WalkMixin:
    def walk(self):
        if hasattr(self, 'title'):
            return f"{self.title} {self.name} {self.gait()} forward"
        return f"{self.name} {self.gait()} forward"


class Person(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"
    
class Noble(WalkingMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return "struts"

class Cat(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"