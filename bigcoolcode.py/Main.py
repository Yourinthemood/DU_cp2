#DU P1 Larose PET SHOP - classes assignement

import json
import os
from pet import Pet
from shop import Shop

class Game:
    def __init__(self):
        self.pet = None
        self.money = 100
        self.inventory = {}
        self.shop = Shop()
    
    def save(self):
        """Save game"""
        data = {
            "money": self.money,
            "inventory": self.inventory,
            "pet_name": self.pet.name if self.pet else None,
            "pet_type": self.pet.pet_type if self.pet else None,
            "hunger": self.pet.hunger if self.pet else None,
            "happiness": self.pet.happiness if self.pet else None,
            "health": self.pet.health if self.pet else None
        }
        with open("save.json", "w") as f:
            json.dump(data, f)
        print("\nGame saved!")
    
    def load(self):
        """Load game"""
        try:
            if os.path.exists("save.json"):
                with open("save.json", "r") as f:
                    data = json.load(f)
                
                if data["pet_name"]:
                    self.pet = Pet(data["pet_name"], data["pet_type"])
                    self.pet.hunger = data["hunger"]
                    self.pet.happiness = data["happiness"]
                    self.pet.health = data["health"]
                
                self.money = data["money"]
                self.inventory = data["inventory"]
                print("\nGame loaded!")
        except:
            print("\nNo save found!")
    
    def show_stats(self):
        """Show pet stats"""
        if not self.pet:
            print("\nCreate a pet first!")
            return
        
        print("\n" + "="*30)
        print(f"{self.pet.name} the {self.pet.pet_type}")
        print(f"Health: {self.pet.health}")
        print(f"Hunger: {self.pet.hunger}")
        print(f"Happiness: {self.pet.happiness}")
        print(f"Money: ${self.money}")
        print("="*30)
    
    def create_pet(self):
        """Create new pet"""
        name = input("Pet name: ")
        print("1. Dog  2. Cat  3. Hamster")
        choice = input("Choose 1-3: ")
        
        types = {"1": "Dog", "2": "Cat", "3": "Hamster"}
        if choice in types:
            self.pet = Pet(name, types[choice])
            print(f"\nCreated {name} the {types[choice]}!")
    
    def feed(self):
        """Feed pet"""
        if not self.pet:
            print("\nNo pet!")
            return
        
        result = self.pet.feed()
        print(f"\n{result}")
        self.money += 10
        print("+$10")
    
    def play(self):
        """Play with pet"""
        if not self.pet:
            print("\nNo pet!")
            return
        
        result = self.pet.play()
        print(f"\n{result}")
        self.money += 15
        print("+$15")
    
    def heal(self):
        """Heal pet"""
        if not self.pet:
            print("\nNo pet!")
            return
        
        if self.money >= 50:
            self.money -= 50
            self.pet.heal()
            print("\nPet healed!")
        else:
            print("\nNeed $50!")
    
    def shop_menu(self):
        """Shop menu"""
        while True:
            print("\n" + "="*30)
            print("SHOP")
            print(f"Money: ${self.money}")
            items = self.shop.get_items()
            
            item_list = list(items.keys())
            for i in range(len(item_list)):
                name = item_list[i]
                price = items[name]
                print(f"{i+1}. {name} - ${price}")
            
            print(f"{len(items)+1}. Exit")
            
            choice = input("Choice: ")
            
            if choice == str(len(items)+1):
                break
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(item_list):
                    item_name = item_list[idx]
                    price = items[item_name]
                    
                    if self.money >= price:
                        self.money -= price
                        
                        if item_name in self.inventory:
                            self.inventory[item_name] += 1
                        else:
                            self.inventory[item_name] = 1
                        
                        print(f"\nBought {item_name}!")
                    else:
                        print("\nNot enough money!")
                else:
                    print("\nInvalid choice!")
            except:
                print("\nInvalid choice!")
    
    def use_item(self):
        """Use item from inventory"""
        if not self.pet:
            print("\nNo pet!")
            return
        
        if not self.inventory:
            print("\nNo items!")
            return
        
        print("\nINVENTORY:")
        items = list(self.inventory.keys())
        for i in range(len(items)):
            item = items[i]
            print(f"{i+1}. {item} (x{self.inventory[item]})")
        print(f"{len(items)+1}. Cancel")
        
        choice = input("Use which item? ")
        
        try:
            if choice == str(len(items)+1):
                return
            
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                item_name = items[idx]
                
                result = self.pet.use_item(item_name)
                print(f"\n{result}")
                
                self.inventory[item_name] -= 1
                if self.inventory[item_name] == 0:
                    del self.inventory[item_name]
            else:
                print("\nInvalid choice!")
        except:
            print("\nInvalid choice!")
    
    def update_pet(self):
        """Update pet status"""
        if not self.pet:
            return
        
        self.pet.hunger += 5
        if self.pet.hunger > 100:
            self.pet.hunger = 100
            self.pet.health -= 10
        
        if self.pet.health <= 0:
            print("\nYour pet died!")
            self.pet = None
    
    def run(self):
        """Main game loop"""
        print("PET SHOP GAME")
        
        while True:
            print("\n1.Create 2.Stats 3.Feed(+$10) 4.Play(+$15) 5.Heal($50)")
            print("6.Shop 7.Use Item 8.Save 9.Load 10.Quit")
            
            choice = input("Choice: ")
            
            if choice == "1":
                self.create_pet()
            elif choice == "2":
                self.show_stats()
            elif choice == "3":
                self.feed()
            elif choice == "4":
                self.play()
            elif choice == "5":
                self.heal()
            elif choice == "6":
                self.shop_menu()
            elif choice == "7":
                self.use_item()
            elif choice == "8":
                self.save()
            elif choice == "9":
                self.load()
            elif choice == "10":
                self.save()
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice!")
            
            self.update_pet()
game.run()
