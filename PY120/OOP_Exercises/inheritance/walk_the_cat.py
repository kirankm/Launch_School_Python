class WalkMixin:
    def walk(self):
        print("Let's go for a walk!")

class Cat(WalkMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

# Comments show expected output
kitty = Cat('Sophie')
kitty.greet()       # Hello! My name is Sophie!
kitty.walk()        # Let's go for a walk!