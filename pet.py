class Hero:
    def __init__(self, name, keys, inventory):
        self.name = name
        self.keys = keys
        self.inventory = inventory

    def buy(self, item, value):
        self.inventory.append(item)
        self.keys -= value
        print(self.inventory)
Adventurer = Hero("Cubical", 0, [])
Adventurer.buy({"title": "Sword", "atk": 1, "value": 3})
print(Adventurer.__dict__)