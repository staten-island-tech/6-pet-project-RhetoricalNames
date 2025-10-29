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
class User: #Parent class
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
studentthing.display_info()
""" class Pet:
    def __init__(self, name, happiness, hunger):
        self.name = name
        self.__happiness = happiness
        self.__hunger = hunger

    def play(self, time):
        self.__happiness += (random.randint(5,10) + time)
        self.__hunger += (random.randint(5,10) + time)/(2)

    def feed(self, food):
        self.__hunger -= (random.randint(10, 20) - food)
        if self.__hunger < 0:
            self.__hunger = 0

    def status(self):
        print(Pikachu.__happiness)
Pikachu = Pet("Pikachu", 10, 0)
Pikachu.play(5)
Pikachu.feed(10)
Pikachu.status() """