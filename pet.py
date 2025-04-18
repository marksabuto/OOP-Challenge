class Pet:
    """Base class for all virtual pets"""
    
    def __init__(self, name, pet_type="generic"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")
        
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play!")
            
    def get_status(self):
        print(f"\n{self.name}'s status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks: {self.tricks}")
            
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")
        
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} knows no tricks yet.")


class Dog(Pet):
    """Dog subclass"""
    def __init__(self, name):
        super().__init__(name, "dog")
        
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")


class Cat(Pet):
    """Cat subclass"""
    def __init__(self, name):
        super().__init__(name, "cat")
        
    def meow(self):
        print(f"{self.name} says: Meow!")