class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self._store = []

    @property
    def store(self):
        return self._store
    
    def put(self, val):
        self.store.append(val)
        if len(self.store) > self.size:
            self.store.pop(0)

    def get(self):
        if self.store:
            return self.store.pop(0)
        return None


class CircularBuffer:
    def __init__(self, size):
        self.store = [None] * size
        self.index_old = 0
        self.insert_index = 0

    def put(self, val):
        if self.store[self.insert_index] is not None:
            self.index_old = (self.index_old + 1) % len(self.store)
        self.store[self.insert_index] = val    
        self.insert_index = (self.insert_index + 1) % len(self.store)

    def get(self):
        oldest_val = self.store[self.index_old]
        if oldest_val is not None:
            self.index_old = (self.index_old + 1) % len(self.store)
        return oldest_val


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