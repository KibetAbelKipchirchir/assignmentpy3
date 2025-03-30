# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

# Child Class: SmartphonePro inheriting from Smartphone
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, price, camera_quality):
        super().__init__(brand, model, price)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality}MP camera on {self.brand} {self.model}.")

# Parent Class: Vehicle (For Polymorphism Challenge)
class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphic behavior

# Child Classes for Polymorphism
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Test Code
if __name__ == "__main__":
    # Assignment 1: Smartphone Class Test
    print("Smartphone Class Test:")
    basic_phone = Smartphone("Nokia", "3310", 50)
    basic_phone.call("123-456-7890")

    pro_phone = SmartphonePro("iPhone", "14 Pro", 1200, 48)
    pro_phone.call("987-654-3210")
    pro_phone.take_photo()

    print("\nPolymorphism Challenge Test:")
    # Activity 2: Polymorphism Test
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()
