class Shelter:
    def __init__(self):
        self._owners = set()
        self._pets = set()

    @property
    def owners(self):
        return self._owners
    
    @property
    def pets(self):
        return self._pets
    
    def adopt(self, owner, pet):
        owner.adopt(pet)
        self.owners.add(owner)
        self.pets.remove(pet)

    def bring_in_new_pet(self, pet):
        self.pets.add(pet)

    def print_adoptions(self):
        if self.pets:
            self.print_unadopted_pets()
        if self.owners:
            self.print_adopted_pets()
    
    def print_unadopted_pets(self):
        print("The Animal Shelter has the following unadopted pets:")
        for pet in self.pets:
            pet.describe()
        print("")

    def print_adopted_pets(self):
        for owner in self.owners:
            owner.describe()
            print("")

class Pet:
    def __init__(self, type, name):
        self._type = type
        self._name = name

    @property
    def type(self):
        return self._type

    @property
    def name(self):
        return self._name 
    
    def describe(self):
        print(f"a {self.type} named {self.name}")

class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name
    
    @property
    def pets(self):
        return self._pets
    
    def adopt(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)

    def describe(self):
        print(f"{self.name} has adopted the following pets:")
        for pet in self.pets:
            pet.describe()

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

hedwig = Pet('owl', 'Hedwig')


phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.bring_in_new_pet(cocoa)
shelter.bring_in_new_pet(cheddar)
shelter.bring_in_new_pet(darwin)
shelter.bring_in_new_pet(kennedy)
shelter.bring_in_new_pet(sweetie)
shelter.bring_in_new_pet(molly)
shelter.bring_in_new_pet(chester)
shelter.bring_in_new_pet(hedwig)


shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")