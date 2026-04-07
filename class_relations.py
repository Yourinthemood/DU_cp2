#class relation notes

# parent class

class Vehical:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

# child class
class Car(Vehical):
    pass

class Boat(Vehical):
    pass

class Plane(Vehical):

Car = Car("keonigsegg", "Agaera RS")

Boat = Boat("U.S. military", "S.S.SALLY")

Plane = Plane("lockheed Martin", "A-12")

print(Car.brand)
print(Car.model)
Car.move()

print(Boat.brand)
print(Boat.model)
Car.move()

print(Plane.brand)
print(Plane.model)
Car.move()