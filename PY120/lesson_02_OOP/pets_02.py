class Pet:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'


class Dog(Pet):
    def fetch(self):
        return 'fetching!'
    
class Cat(Pet):
    pass

kitty = Cat()
print(kitty.run())

doggy = Dog()
print(doggy.run())
print(doggy.fetch())

print(kitty.fetch())