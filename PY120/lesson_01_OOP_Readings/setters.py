class Dog():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

sparky = Dog('sparky', 5)

sparky = Dog('Sparky', 5)
print(sparky.name)          # Sparky
print(sparky.age)           # 5
sparky.name = 'Fireplug'
print(sparky.name)          # Fireplug
sparky.age = 6
print(sparky.age)