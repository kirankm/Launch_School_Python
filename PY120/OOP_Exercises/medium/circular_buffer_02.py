import pdb

class Value:
    def __init__(self, value):
        self.value = value

    @property
    def next(self):
        if hasattr(self, '_next'):
            return self._next
        return None
    
    @next.setter
    def next(self, next_value):
        if isinstance(next_value, Value):
            self._next = next_value
        else:
            raise TypeError("Only items of type Value can be given as next item")
    
    @property
    def previous(self):
        if hasattr(self, '_previous'):
            return self._previous
        return None
    
    @previous.setter
    def previous(self, prev_value):
        self._previous = prev_value
        if isinstance(prev_value, Value):
            prev_value.next = self

    @property
    def index(self):
        if hasattr(self, '_index'):
            return self._index
        return None
    
    @index.setter
    def index(self, index):
        self._index = index

class CircularBuffer:
    @classmethod
    def get_circular_index(cls, curr_index, size):
        return (curr_index + 1) % size

    def __init__(self, size):
        self.shape = [None] * size
        self.oldest = None
        self.last = None

    def put(self, new_value):
        new_value = Value(new_value)
        new_value.previous = self.last
        next_index = self.get_next_index()
        if self.shape[next_index]:
            self.shape[self.oldest.index] = new_value
            new_value.index = self.oldest.index
            self.oldest = self.oldest.next
        else:
            self.shape[next_index] = new_value
            new_value.index = next_index
        self.last = new_value
        if self.oldest is None:
            self.oldest = new_value

    def get(self):
        if self.oldest is None:
            return None
        curr_old = self.oldest
        self.oldest = self.oldest.next
        if self.oldest:
            self.oldest.previous = None
        self.shape[curr_old.index] = None
        return curr_old.value

    def get_next_index(self):
        if self.last is None:
            return 0
        last_index = self.last.index
        size = len(self.shape)
        return CircularBuffer.get_circular_index(last_index, size)
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)

print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
