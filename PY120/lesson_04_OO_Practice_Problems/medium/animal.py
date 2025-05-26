class Animal:
    def speak(self, msg):
        print(msg)
    
class Cat(Animal):
    def meow(self):
        self.speak("Meow!!")

class Dog(Animal):
    def bark(self):
        self.speak("Woof!!")


cat = Cat()
dog = Dog()

cat.meow()
dog.bark()