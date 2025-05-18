class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    @name.setter
    def name(self, p_name):
        name_lst = p_name.split()
        self.first_name = name_lst[0]
        self.last_name = '' if len(name_lst) == 1 else name_lst[1]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, f_name):
        self._first_name = f_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, l_name):
        self._last_name = l_name

    def __str__(self):
        return self.name


bob = Person('Robert Smith')
print(f"The person's name is: {bob}")