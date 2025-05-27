class Vehicle:
    def __init__(self, brand, model, year, color, seats, max_speed, mileage, fuel_type,bus_fare):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.seats = seats
        self.max_speed = max_speed
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.bus_fare = bus_fare

class Bus(Vehicle):
    pass    

school_bus =  Bus("Volvo", "B8R", 2011, "yellow", 60, 150, 200000, "hybrid-electric", 1200)



