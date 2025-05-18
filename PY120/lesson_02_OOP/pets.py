class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

class BullDog(Dog):
    def sleep(self):
        return 'snoring!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

karl = BullDog()
print(karl.speak())       # bark!
print(karl.sleep())        # snoring!