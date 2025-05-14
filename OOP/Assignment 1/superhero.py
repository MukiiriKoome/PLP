class Superhero:
    def __init__(self, name, power, secret_identity):
        # Encapsulation: Protected attributes
        self._name = name
        self._power = power
        self._secret_identity = secret_identity
    
    # Method to display info
    def introduce(self):
        print(f"Hero: {self._name}, Power: {self._power}, Secret Identity: {self._secret_identity}")
    
    # Polymorphic method (override in subclasses)
    def use_power(self):
        print(f"{self._name} uses {self._power}!")

# Inheritance: Subclass for a specific hero type
class TechHero(Superhero):
    def __init__(self, name, power, secret_identity, gadget):
        super().__init__(name, power, secret_identity)
        self.gadget = gadget  # Additional attribute
    
    # Polymorphism: Override use_power()
    def use_power(self):
        print(f"{self._name} activates {self.gadget} to {self._power}!")

# Example Usage
if __name__ == "__main__":
    hero1 = Superhero("Thor", "lightning", "Thor Odinson")
    hero1.introduce()          # Output: Hero: Thor, Power: lightning, Secret Identity: Thor Odinson
    hero1.use_power()          # Output: Thor uses lightning!

    hero2 = TechHero("Iron Man", "repulsor beams", "Tony Stark", "nanotech suit")
    hero2.introduce()          # Output: Hero: Iron Man, Power: repulsor beams, Secret Identity: Tony Stark
    hero2.use_power()          # Output: Iron Man activates nanotech suit to repulsor beams!
