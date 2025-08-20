##PEDAC
'''
ClassMethods

Instance Methods
init
    input: List

is_empty: bool

contains: bool
    checks if value exists

is_subset: bool
    input: another set
    Empty set is subset of all sets

is_disjoint: bool
    input: another set
    empty set is disjoint with all sets
    if shared element exists return false

is_same: bool
    input:another set
    elements same return True

add: return None
    input: int

intersection: return common value set
    input another set

difference: return difference set Empty set if both operand same
    input another set
    
union

Instance Variables

Properties
'''

class CustomSet:
    def __init__(self, lst = None):
        self._elements = []
        lst = lst if lst else []
        for val in lst:
            self.add(val)

    @property
    def elements(self):
        return self._elements
    
    @property
    def len(self):
        return len(self.elements)
    
    def add(self, value):
        if not self.contains(value):
            self.elements.append(value)
    
    def contains(self, value):
        return value in self.elements
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def is_subset(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        for val in self.elements:
            if not other.contains(val):
                return False
        return True
    
    def is_disjoint(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        for val in self.elements:
            if other.contains(val):
                return False
        return True
    
    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        return (self.len == other.len) and (self.len == self.intersection(other).len)
    
    def is_same(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        return self == other
    
    def intersection(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        intersection_list = [val for val in self.elements if other.contains(val)]
        return CustomSet(intersection_list)
    
    def difference(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        difference_list = [val for val in self.elements if not other.contains(val)]
        return CustomSet(difference_list)
    
    def union(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        union_lst = self.elements + other.elements
        return CustomSet(union_lst)


    