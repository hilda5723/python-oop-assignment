
# -----------------------------------------------
# Assignment 1: Design Your Own Class 🏗️
# Create a class representing anything (e.g., Smartphone).
# Add attributes, methods, constructors, and inheritance.
# -----------------------------------------------

# Step 1: Define the base class "Smartphone"
class Smartphone:
    # Step 2: Constructor to initialize attributes
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Step 3: Method to simulate calling a number
    def call(self, number):
        print(f"{self.model} is calling {number}...")

    # Step 4: Method to display smartphone information
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")


# Step 5: Create a subclass using Inheritance (Polymorphism & Encapsulation)
class GamingPhone(Smartphone):
    # Step 6: Add a new attribute (gpu) using constructor and call parent constructor
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    # Step 7: New method specific to GamingPhone
    def play_game(self, game):
        print(f"Playing '{game}' on {self.model} using GPU: {self.gpu}")

    # Step 8: Override display_info method to include GPU info (Polymorphism)
    def display_info(self):
        super().display_info()
        print(f"GPU: {self.gpu}")


# Step 9: Create objects and test the class functionality

# Creating a regular smartphone
phone1 = Smartphone("Samsung", "Galaxy A14", 250)
print("---- Regular Smartphone ----")
phone1.display_info()
phone1.call("0712345678")

print("\n---- Gaming Smartphone ----")
# Creating a gaming smartphone
gaming = GamingPhone("Asus", "ROG 5", 800, "Adreno 660")
gaming.display_info()
gaming.play_game("PUBG")



#Assignment 2 – Polymorphism

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Example usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
