'''
PEDAC
input : 3 parameters
Output : an instance of the triangle class

Understanding
Class should have an attribute called kind
    Kind can be : "equilateral", "isosceles" or "scalene"
No input param can be less than or equal to 0
Sum of 2 sides have to be greater than third side
'''

class Triangle:
    def __init__(self, a, b, c):
        sides = Triangle.validate_sides(a,b,c)
        self.min_side = sides[0]
        self.max_side = sides[2]
        self.middle_side = sides[1]
        self.kind = self._get_triangle_kind()

    def _get_triangle_kind(self):
        if self.min_side == self.max_side:
            return "equilateral"
        if self.min_side == self.middle_side:
            return "isosceles"
        if self.max_side == self.middle_side:
            return "isosceles"
        else:
            return "scalene"

    @staticmethod
    def validate_sides(a,b,c):
        sides = sorted((a,b,c))
        if sides[0] <= 0:
            raise ValueError("Only positive values allowed for triangle sides")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid Values for Sides!!. Sum of any 2 sides should be greater than third side")
        return sides
        
    

    