###PEDAC
'''
class SimpleLinkedList
init
    takes no values

properties
size: returns length
head: last inserted element
    should be an element

methods
is_emtpy
    boolean

push 
    input
        datum
    add element
peek
    none if no element
    else last inserted element's value
pop
    same as list pop
from_list:
    input: list: can be empty also
        None also is a possible value
    generate a linked list
    if empty list size should be 0
    if None list size should be 0
to_list:
    convert to a list
reverse




class Element
- init
    datum
    next element: Default none
- datum : data
- is_tail()
    boolean
    check if it's the last value in the linked list
- next
    property?
    return None if no element, (tail) else return that element

'''

class Element:
    def __init__(self, datum, next = None):
        self.datum = datum
        self.next = next

    def is_tail(self):
        return self.next is None
    
class SimpleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        new_element = Element(value, self.head)
        self.head = new_element
        self.size += 1

    def peek(self):
        return None if self.head is None else self.head.datum
    
    def pop(self):
        pop_el = self.head
        self.head = pop_el.next
        self.size -= 1
        return pop_el.datum
    
    @classmethod
    def from_list(cls, new_list):
        linked_list = cls()
        if new_list is None:
            return linked_list
        for value in new_list[::-1]:
            linked_list.push(value)
        return linked_list
    
    def to_list(self):
        out_lst = []
        curr_el = self.head
        while curr_el is not None:
            out_lst.append(curr_el.datum)
            curr_el = curr_el.next
        return out_lst
    
    def reverse(self):
        lst = self.to_list()
        return SimpleLinkedList.from_list(lst[::-1])

