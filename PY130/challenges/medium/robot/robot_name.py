# PEDAC
'''
P: No input
Output:
    Robot Class:
        name: instance variable: 
            Should be random
            Should remain the same until reset
            if name already taken, should assign new name
'''

import random
import string

class Robot:
    current_names = set()
    @staticmethod
    def get_random_character():
        return random.choice(string.ascii_uppercase)

    @staticmethod
    def get_random_number():
        return random.choice(string.digits)
    
    @classmethod
    def get_random_name(cls):
        name_string = cls.get_random_character() + cls.get_random_character()
        name_number = cls.get_random_number() + cls.get_random_number() + cls.get_random_number()
        name = name_string + name_number
        return name
    
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is None:
            self.assign_name()
        return self._name

    @name.setter
    def name(self, name):
        if name in self.__class__.current_names:
            raise ValueError("Name already exists")
        self._name = name
        self.__class__.current_names.add(name)

    def assign_name(self):
        new_name = self.get_random_name()
        while new_name in self.__class__.current_names:
            new_name = self.get_random_name()
        self.name = new_name

    def reset(self):
        self.__class__.current_names.remove(self.name)
        self._name = None

    