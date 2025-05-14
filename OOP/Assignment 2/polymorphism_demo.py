class Animal:
    def move(self):
        pass  # Abstract method

class Bird(Animal):
    def move(self):
        print("Flying high!")

class Fish(Animal):
    def move(self):
        print("Swimming deep!")

class Vehicle:
    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def move(self):
        print("Driving on roads!")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

# Polymorphism in action
def demonstrate_movement(entity):
    entity.move()

# Example Usage
if __name__ == "__main__":
    animals = [Bird(), Fish()]
    vehicles = [Car(), Plane()]

    print("--- Animals ---")
    for animal in animals:
        demonstrate_movement(animal)  # Output: Flying high! / Swimming deep!

    print("--- Vehicles ---")
    for vehicle in vehicles:
        demonstrate_movement(vehicle)  # Output: Driving on roads! / Flying in the sky!
