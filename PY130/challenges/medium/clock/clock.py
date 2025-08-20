### PEDAC
'''
Input
Clock class
    Classmethods
        at 
            input hour, minute
                Minute by default is 0
            Output clock object
Clock Instance
    has hour and minute
    str clock 
        will show "HH:MM"

    Addition
        Returns a new clock object

    Subtraction
        Returns a new clock object

    Equality
        Compares the string representation
'''

class Clock:
    @classmethod
    def at(cls, hour, minute = 0):
        return Clock(hour, minute)

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def hour(self, new_hour):
        self._hour = new_hour % 24

    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def minute(self, new_minute):
        self._minute = new_minute % 60

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"
    
    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return str(self) == str(other)
    
    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        hour, minute = divmod(other, 60)
        new_hour = self.hour + hour
        new_minute = self.minute + minute
        return Clock(new_hour, new_minute)
        
    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        curr_time = 60 * self.hour + self.minute
        new_time = curr_time - other
        hour, minute = divmod(new_time, 60)
        return Clock(hour, minute)