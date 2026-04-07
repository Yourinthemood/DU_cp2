from faker import Faker
import random

class QuickRandom:
    def __init__(self):
        self.fake = Faker()
    
    def character(self, classes, races):
        return {
            "name": self.fake.first_name() + " " + self.fake.last_name(),
            "class": random.choice(classes)['name'],
            "level": random.randint(1, 10),
            "race": random.choice(races)['name'],
            "attributes": [],
            "base_attributes": [random.randint(5, 15) for _ in range(5)],
            "skills": set(),
            "skill_levels": {},
            "inventory": [],
            "backstory": f"Born in {self.fake.city()}, {self.fake.country()}",
            "location": self.fake.city(),
            "personality": random.choice(['Brave', 'Wise', 'Sneaky', 'Loyal', 'Mysterious'])
        }
    
    def quest(self):
        return f"Defeat the monster in {self.fake.city()}"
