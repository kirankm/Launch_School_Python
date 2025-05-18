class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return f'I am {self.name}'

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)   