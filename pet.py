import random
class Pet:
    def __init__(self, name, happiness, hunger, hygiene, rest, thirst, age, status):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.hygiene = hygiene
        self.rest = rest
        self.thirst = thirst
        self.age = age
        self.status = status

    def play(self):
        playing = (random.randint(5,15))
        self.happiness += playing
        self.hunger += (playing/2)
        self.hygiene -= playing
        self.rest -= 5
        self.age += 1
        print(f"You play with '{self.name}', increasing happiness to {self.happiness}. Hunger increased to {self.hunger}, hygiene decreased to {self.hygiene}, and happiness to {self.happiness}.")

    def feed(self):
        feed = random.randint(10, 20)
        self.hunger -= feed
        self.hygiene -= 5
        self.rest -= 5
        self.age += 1
        self.happiness -= 5
        if self.hunger < 0:
            self.hunger = 0
        print(f"You feed '{self.name}', decreasing hunger to {self.hunger}. Hygiene decreased to {self.hygiene} and happiness to {self.happiness}.")
    
    def clean(self):
        self.hygiene += 15
        self.happiness -= 5
        self.age += 1
        self.rest -= 5
        if self.hygiene > 50:
            self.hygiene = 50
        if self.hygiene <= 0:
            self.hygiene = 0
        print(f"You wash '{self.name}', increasing hygiene to {self.hygiene}. Happiness decreased to {self.happiness}.")

    def sleep(self):
        self.rest += 20
        self.hygiene -= 5
        self.hunger += 10
        self.thirst += 10
        self.happiness -= 5
        self.age += 1
        if self.rest > 60:
            self.rest = 60
        print(f"'{self.name}' sleeps. Rest increased to {self.rest}. Hygiene decreased to {self.hygiene}, happiness decreased to {self.happiness}, hunger increased to {self.hunger} and thirst to {self.thirst}.")

    def drink(self):
        self.thirst -= 15
        self.hygiene -= 5
        self.rest -= 5
        self.age += 1
        self.happiness -= 5
        if self.thirst < 0:
            self.thirst = 0
        print(f"'{self.name}' drinks water. Thirst decreased to {self.thirst}. Hygiene and happiness decreased to {self.hygiene} and {self.happiness}.")

    def self_check(self):
        if self.hunger >= 125:
            print(f"'{self.name}' starved to death!")
            self.status = "Dead"
        if self.thirst >= 125:
            print(f"'{self.name}' died of thirst!")
            self.status = "Dead"
        if self.hunger >= 75:
            self.happiness -= 10
            print(f"'{self.name}' is starving! Happiness decreased to {self.happiness}.")
        if self.thirst >= 75:
            self.happiness -= 10
            print(f"'{self.name}' needs water! Happiness decreased to {self.happiness}.")
        if self.rest <= 0:
            self.rest += 20
            self.happiness -= 15
            print(f"'{self.name}' needs to rest! Happiness decreased to {self.happiness}.")
        if self.hygiene == 0:
            self.happiness -= 20
            print(f"'{self.name}' is very dirty! Happiness decreased to {self.happiness},")
        if self.happiness <= 0:
            self.status = "Grown"
            print(f"{self.name}'s happiness dropped too low!")
        print(f"Happiness: {self.happiness}. Hunger: {self.hunger}/75. Hygiene: {self.hygiene}/50. Rest: {self.rest}/60. Thirst: {self.thirst}/75.")

options = ["Play", "Feed", "Clean", "Sleep", "Drink"]
pet = Pet("Name not given!", 20, 30, 50, 25, 30, 0, "Not grown")
pet.name = input("You are taking care of a creature you found while scavenging. Your goal is to keep it alive and happy. What would you like to name it?")
print("Here are your options: (Note - most actions decrease happiness - choose wisely!)")
while pet.status == "Not grown":
    for index, item in enumerate(options, start = 1):
        print(index, ":", item)
    choice = input(f"What would you like to do? '{pet.name}' is {pet.age} days old.")
    if not choice.isdigit():
        print("Invalid input. Please try again.")
    else:
        choice = int(choice)
    if choice == 1:
        pet.play()
        pet.self_check()
    elif choice == 2:
        pet.feed()
        pet.self_check()
    elif choice == 3:
        pet.clean()
        pet.self_check()
    elif choice == 4:
        pet.sleep()
        pet.self_check()
    elif choice == 5:
        pet.drink()
        pet.self_check()
"""     print(f"You selected {options[choice]}.")
    print(pet.__dict__[choice]) """
""" def guard_clause(a, b):
    a = 1 if b["class"] else 0
    return cost * (1 - a) """
