class Foo():
    def __init__(self):
        pass


a = Foo()
b = Foo()

print(type(a).__name__)
print(b.__class__.__name__)