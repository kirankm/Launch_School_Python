class Cat:
    def __init__(self):
        pass

    def get_name(self):
        try:
            return self.name
        except:
            print("Not set")
    
tom = Cat()
print(tom.get_name())