class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return self.first_name + " " + self.last_name
    
    @name.setter
    def name(self, name_tuple):
        first_name, last_name = name_tuple
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name.capitalize()
    
    @first_name.setter
    def first_name(self, first_name):
        if first_name.isalpha():
            self._first_name = first_name
        else:
            raise ValueError("First Name must be Alphabetic")

    @property
    def last_name(self):
        return self._last_name.capitalize()
    
    @last_name.setter
    def last_name(self, last_name):
        if last_name.isalpha():
            self._last_name = last_name
        else:
            raise ValueError("Last Name must be Alphabetic")

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel


character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall


friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.

