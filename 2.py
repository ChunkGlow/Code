class Fare:

    busName = "Bus 1"
    busNumber = 1
    busType = "City Bus"
    busCapacity = 50
    busFare = 4.75
    busRoute = "Downtown to Uptown"

    
    def __init__(self, fare, bus):
        self.fare = fare
        self.bus = bus

busfare = Fare.busFare
bus = Fare.busName
a = Fare(4.75, "Bus 1")

print(busfare)
print(bus)


