class Car:
    def __init__(self, name, year):
        self._name = name
        self._year = year

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def show_details(self):
        print(f"This is a {self._year} {self._name}")

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return (self.name == other.name) and (self._year == other._year)