import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        x_val = self.x * other.x
        y_val = self.y * other.y
        return x_val + y_val
    
    def __abs__(self):
        x_val = self.x ** 2
        y_val = self.y ** 2
        abs_sqrd = x_val + y_val
        return math.sqrt(abs_sqrd)
        

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)
print(v1 - v2) 
print(v1 * v2) # 17
print(abs(v1)) # 13.0
