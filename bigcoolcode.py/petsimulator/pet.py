#life is roblox
''' I took lots of inspiration from indie games which made it easier to finish this '''
class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 50
        self.happiness = 50
        self.health = 100
    
    def feed(self):
        self.hunger -= 30
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        return f"{self.name} ate! Hunger: {self.hunger}"
    
    def play(self):
        if self.hunger > 80:
            return f"{self.name} is too hungry to play!"
        
        self.happiness += 25
        if self.happiness > 100:
            self.happiness = 100
        self.hunger += 15
        if self.hunger > 100:
            self.hunger = 100
        return f"{self.name} played! Happiness: {self.happiness}"
    
    def heal(self):
        self.health += 30
        if self.health > 100:
            self.health = 100
        return f"{self.name} healed! Health: {self.health}"
    
    def use_item(self, item_name):
        if "Treat" in item_name:
            self.happiness += 20
            if self.happiness > 100:
                self.happiness = 100
            return f"{self.name} is happier! +20 happiness"
        elif "Medicine" in item_name:
            self.health += 25
            if self.health > 100:
                self.health = 100
            return f"{self.name} feels better! +25 health"
        elif "Food" in item_name:
            self.hunger -= 40
            if self.hunger < 0:
                self.hunger = 0
            self.happiness += 15
            if self.happiness > 100:
                self.happiness = 100
            return f"{self.name} ate premium food!"
        return f"Used {item_name}!"
