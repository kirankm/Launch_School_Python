class CircularBuffer:
    def __init__(self, size):
        self.store = [None] * size
        self.oldest_pos = 0
        self.last_pos = None

    def get_next_index(self, curr_index):
        if curr_index is None:
            return 0
        size = len(self.store)
        return (curr_index + 1) % size

    def put(self, val):
        put_index = self.get_next_index(self.last_pos)
        self.last_pos = put_index
        if self.store[put_index]:
            self.oldest_pos = self.get_next_index(self.oldest_pos)
        self.store[put_index] = val
    
    def get(self):
        if self.store[self.oldest_pos] is None:
            return None
        old_val = self.store[self.oldest_pos]
        self.store[self.oldest_pos] = None
        self.oldest_pos = self.get_next_index(self.oldest_pos)
        return old_val


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