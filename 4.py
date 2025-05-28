class Car:
    def __car_model__(self, brand, model, year, plugin, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.plugin = plugin
        self.color = color
        self.price = price

    def __engine__(self, fuel_type, engine, horespower, torque):
        self.engine = engine
        self.fuel_type = fuel_type
        self.horespower = horespower
        self.torque = torque

    def __speed__(self, max_speed, acceleration):
        self.max_speed = max_speed
        self.acceleration = acceleration

    
class BMW(Car):
    def __init__(self, brand, model, year, plugin, color, price, fuel_type, engine, horespower, torque, max_speed, acceleration):
        self.__car_model__(brand, model, year, plugin, color, price)
        self.__engine__(fuel_type, engine, horespower, torque)
        self.__speed__(max_speed, acceleration)

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Plugin: {self.plugin}, Color: {self.color}, Price: {self.price}")
        print(f"Fuel Type: {self.fuel_type}, Engine: {self.engine}, Horsepower: {self.horespower}, Torque: {self.torque}")
        print(f"Max Speed: {self.max_speed}, Acceleration: {self.acceleration}")

# Example usage

my_bmw = BMW("BMW", "X5", 2022, "Hybrid", "Black", 60000, "Petrol", "V8", 400, 550, 250, 5.0)
my_bmw.display_info()

# This code defines a class hierarchy for a car, specifically a BMW, with methods to set and display various attributes.

# The BMW class inherits from the Car class and initializes its attributes through the parent class methods.

# The display_info method prints out the car's details in a formatted manner.
# The example usage creates an instance of the BMW class and displays its information.
# The code is structured to allow for easy extension and modification of car attributes and behaviors.
        
    