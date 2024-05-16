class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name_, hunger_=0):
        self._name = name_
        self._hunger = hunger_

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1
    
    def type(self):
        return "animal"
    
    def talk(self):
        pass
    def special_ability(self):
        pass
    
class Dog(Animal):
    def __init__(self, name_, hunger_=0):
        super().__init__(name_, hunger_)
    def type(self):
        return "Dog"
    def talk(self):
        return "woof woof"
    def fetch_stick(self):
        print("There you go, sir!")
    def special_ability(self):
        self.fetch_stick()
        
class Cat(Animal):
    def __init__(self, name_, hunger_=0):
        super().__init__(name_, hunger_)
    def type(self):
        return "Cat"
    def talk(self):
        return "meow"
    def chase_laser(self):
        print("Meeeeow")
    def special_ability(self):
        self.chase_laser()
class Skunk(Animal):
    def __init__(self, name_, hunger_= 0, _stink_count = 6):
        super().__init__(name_, hunger_)
        self._stink_count = _stink_count
    def type(self):
        return "Skunk"
    def talk(self):
        return "tsssss"
    def stink(self):
        print("Dear lord!")
    def special_ability(self):
        self.stink()
class Unicorn(Animal):
    def __init__(self, name_, hunger_=0):
        super().__init__(name_, hunger_)
    def type(self):
        return "Unicorn"
    def talk(self):
        return "Good day, darling"
    def sing(self):
        print("Im not your toy...")
    def special_ability(self):
        self.sing()
class Dragon(Animal):
    def __init__(self, name_, hunger_= 0, _color = "Green"):
        super().__init__(name_, hunger_)
        self._color = _color
    def type(self):
        return "Dragon"
    def talk(self):
        return "Raaaawr"
    def breath_fire(self):
        print("$@#$#@$")
    def special_ability(self):
        self.breath_fire()

if (__name__ == "__main__"):
    dog = Dog("Brownie", 10)
    dog2 = Dog("Doggo", 80)
    cat = Cat("Zelda", 3)
    cat2 = Cat("Kitty", 80)
    skunk = Skunk("Stinky")
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn = Unicorn("Keith", 7)
    unicorn2 = Unicorn("Clair", 80)
    dragon = Dragon("Lizzy", 1450)
    dragon2 = Dragon("McFly", 80)
    zoo_lst = [dog, dog2, cat, cat2, skunk, skunk2, unicorn, unicorn2, dragon, dragon2]
    for animal in zoo_lst:
        if animal.is_hungry():
            print("type :" , animal.type(), ",name :", animal.get_name())
            while(animal.is_hungry()):
                animal.feed()
        print(animal.talk())
        animal.special_ability()
    print("Zoo name:", Animal.zoo_name)