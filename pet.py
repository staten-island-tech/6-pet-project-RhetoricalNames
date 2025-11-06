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

#L2
""" class User: #Parent class
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Student(User): #Child class, calls parent class
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        print(f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}")
studentthing = Student("csmajor", "csmajor@email.com", "1234567890")
studentthing.display_info() """
class Pet:
    def __init__(self, name, happiness, hunger, hygiene, rest, thirst, age, growth):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.hygiene = hygiene
        self.rest = rest
        self.thirst = thirst
        self.age = age
        self.growth = growth

    def play(self):
        playing = (random.randint(5,15))
        self.happiness += playing
        self.hunger += (playing/2)
        self.hygiene -= playing
        self.rest -= 5
        self.age += 1
        print(f"Happiness increased to {self.happiness}. Hunger increased to {self.hunger}, and hygiene decreased to {self.hygiene}.")

    def feed(self):
        feed = random.randint(10, 20)
        self.hunger -= feed
        self.hygiene -= 5
        self.rest -= 5
        self.age += 1
        if self.hunger < 0:
            self.hunger = 0
        print(f"Hunger decreased to {self.hunger}. Hygiene decreased to {self.hygiene}.")
    
    def clean(self):
        self.hygiene += 15
        self.happiness -= 5
        self.age += 1
        self.rest -= 5
        if self.hygiene > 50:
            self.hygiene = 50
        print(f"Hygiene increased to {self.hygiene}. Happiness decreased to {self.happiness}.")

    def sleep(self):
        self.rest += 20
        self.hygiene -= 5
        self.hunger += 10
        self.thirst += 10
        self.age += 1
        print(f"Rest increased to {self.rest}. Hygiene decreased to {self.hygiene}, hunger increased to {self.hunger} and thirst to {self.thirst}.")

    def drink(self):
        self.thirst -= 15
        self.hygiene -= 5
        self.rest -= 5
        self.age += 1
        print(f"Thirst decreased to {self.thirst}. Hygiene also decreased to {self.hygiene}.")

    def self_status(self):
        print(f"Happiness: {self.happiness}. Hunger: {self.hunger}/75. Hygiene: {self.hygiene}/50. Rest: {self.rest}/40. Thirst: {self.thirst}/75.")

    def self_check(self):
        if self.hunger >= 125:
            print(f"'{self.name}' starved to death!")
            self.growth = "Dead"
        if self.thirst >= 125:
            print(f"'{self.name}' died of thirst!")
            self.growth = "Dead"
        if self.hunger >= 75:
            self.happiness -= 10
            print(f"'{self.name}' is starving! Happiness decreased to {self.happiness}.")
        if self.thirst >= 75:
            self.happiness -= 10
            print(f"'{self.name}' needs water! Happiness decreased to {self.happiness}.")
        if self.rest <= 0:
            self.rest += 20
            self.happiness -= 25
            print(f"'{self.name}' needs to rest! Happiness decreased to {self.happiness}.")
        if self.hygiene >= 50:
            self.happiness -= 15
            print(f"'{self.name}' is very dirty! Happiness decreased to {self.happiness},")
        if self.happiness <= 0:
            self.growth = "Grown"
            print(f"{self.name}'s happiness dropped too low, and grew to adult size!")

options = [{"Play"}, {"Feed"}, {"Clean"}, {"Sleep"}, {"Drink"}, {"Check pet status"}]
pet = Pet("Name not given!", 20, 30, 50, 25, 30, 0, "Not grown")
pet.name = input("You are taking care of a creature you found while scavenging. Your goal is to keep it alive and happy. What would you like to name it?")
while pet.growth == "Not grown":
    for index, item in enumerate(options, start = 1):
        print(index, ":", item)
    choice = input(f"What would you like to do? '{pet.name}' is {pet.age} days old.")
    if not choice.isdigit():
        print("Invalid input. Please try again.")
    else:
        choice = int(choice)
    if choice == 1:
        pet.play()
    elif choice == 2:
        pet.feed()
        pet.self_check()
    elif choice == 3:
        pet.clean()
        pet.self_check()
    elif choice == 4:
        pet.sleep()
    elif choice == 5:
        pet.drink()
        pet.self_check()
    elif choice == 6:
        pet.self_status()
"""     print(f"You selected {options[choice]}.")
    print(pet.__dict__[choice]) """
""" def guard_clause(a, b):
    a = 1 if b["class"] else 0
    return cost * (1 - a) """
