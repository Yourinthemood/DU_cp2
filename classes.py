#Du classes notes

#example 1 
class animal:
    def _init_(self, name, species, age):
        self.name = name 
        self.species = species
        self.age = age

    print(f"""name = {self.name})
    species = {self.species}
    age = {self.age}""")

    dog = animal("doug", "dog", 4)