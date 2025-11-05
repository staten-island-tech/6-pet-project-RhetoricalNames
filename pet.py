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
        self.__name = name
        self.__happiness = happiness
        self.__hunger = hunger
        self.__hygiene = hygiene
        self.__rest = rest
        self.__thirst = thirst
        self.__age = age
        self.__growth = growth

    def play(self):
        playing = (random.randint(5,15))
        self.__happiness += playing
        self.__hunger += (playing/2)
        self.__hygiene -= playing
        self.__rest -= 5
        self.__age += 1
        print(f"Happiness increased by {playing}. Hunger increased by {(playing/2)}, and hygiene decreased by {playing}.")

    def feed(self):
        feed = random.randint(10, 20)
        self.__hunger -= feed
        self.__hygiene -= 5
        self.__rest -= 5
        self.__age += 1
        if self.__hunger < 0:
            self.__hunger = 0
        print(f"Hunger decreased to {self.__hunger}. Hygiene decreased by 5.")
    
    def clean(self):
        self.__hygiene += 15
        self.__happiness -= 5
        self.__age += 1
        self.__rest -= 5
        if self.__hygiene > 50:
            self.__hygiene = 50
        print(f"Hygiene increased to {self.__hygiene}. Happiness decreased to {self.__happiness}.")

    def sleep(self):
        self.__rest += 20
        self.__hygiene -= 5
        self.__hunger += 10
        self.__thirst += 10
        self.__age += 1
        print(f"Rest increased by {self.__rest}. Hygiene decreased by 5, hunger and thirst increased by 10.")

    def drink(self):
        self.__thirst -= 15
        self.__hygiene -= 5
        self.__rest -= 5
        self.__age += 1
        print(f"Thirst decreased by 15. Hygiene also decreased by 5.")

    def self_status(self):
        print(self.__dict__)

    def happiness_check(self):
        if self.__happiness <= -10:
            self.__growth = "Grown."

options = [{"Play"}, {"Feed"}, {"Clean"}, {"Sleep"}, {"Drink"}, {"Check pet status"}]
pet = Pet("Name not given!", 20, 0, 50, 25, 50, 5)
pet.__growth = "Not grown."
pet.__name = input("You are taking care of a creature you found while scavenging. Your goal is to keep it happy, for as long as possible. What would you like to name it?")
pet.__age = 5
while pet.__growth == "Not grown.":
    for index, item in enumerate(options, start = 1):
        print(index, ":", item)
    choice = input(f"What would you like to do? '{pet.__name}' is {pet.__age} days old.")
    if not choice.isdigit():
        print("Invalid input. Please try again.")
    else:
        choice = int(choice)
    if choice == 1:
        pet.play()
    elif choice == 2:
        pet.feed()
        pet.happiness_check()
    elif choice == 3:
        pet.clean()
        pet.happiness_check()
    elif choice == 4:
        pet.sleep()
    elif choice == 5:
        pet.drink()
        pet.happiness_check()
    elif choice == 6:
        pet.self_status()
"""     print(f"You selected {options[choice]}.")
    print(pet.__dict__[choice]) """
""" def guard_clause(a, b):
    a = 1 if b["class"] else 0
    return cost * (1 - a) """