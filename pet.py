import random

#L1-5(1)
""" class Hero:
    def __init__(self, name, keys, inventory):
        self.name = name
        self.keys = keys
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Adventurer = Hero("Cubical", 0, [])
Adventurer.buy({"title": "Sword", "atk": 1})
print(Adventurer.__dict__) """

class Pet:
    def __init__(self, name, happiness, hunger):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger

    def play(self, time):
        self.happiness += (random.randint(5,10) + time)
        self.hunger += (random.randint(5,10) + time)/(2)

    def feed(self, food):
        self.hunger -= (random.randint(10, 20) - food)
        if self.hunger < 0:
            self.hunger = 0

    def status(self):
        print(Pikachu.hunger)
        print(Pikachu.happiness)
Pikachu = Pet("Pikachu", 10, 0)
Pikachu.play(5)
Pikachu.feed(10)
print(Pikachu.__dict__)