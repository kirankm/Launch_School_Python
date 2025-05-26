class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed
    
poodle = Dog('Poodle')
g_r = Dog('Golden Retriever')

print(poodle.get_breed())
print(g_r.get_breed())

poodle._breed = "spaniel"
print(poodle.get_breed())