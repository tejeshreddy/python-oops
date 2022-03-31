"""
parking lot has 2 levels
each level has 2 rows
each row has two parking slots
car will tkae one parking slot
"""

class Car:
    def __init__(self, license_number):
        self.license_number = license_number

class ParkingSlot:
    def __init__(self, row, spotNumber, level, car):
        self.row = row
        self.spotNumber = spotNumber
        self.level = level
        self.car = car
    
    def isAvailable(self):
        return self.car == None
    
    def park(self, vehicle):
        self.car = vehicle
    
    def removeVehicle(self):
        self.car = None

class Level:
    def __init__(self, rows, levelNumber):
        self.levelNumber = levelNumber
        self.rows = rows
        self.spotsPerRow = 2
        self.parkingSlots = []
        self.availableSpots = rows * self.spotsPerRow
    
    def findAvailableSlots(self):
        if self.availableSpots <= 0:
            return None
        
        if len(self.parkingSlots) == 0:
            return ParkingSlot(0, 0, 0, None)
        else:
            lastCarParked = self.parkingSlots[-1]
        
        if lastCarParked.spotNumber < self.spotsPerRow:
            return ParkingSlot(lastCarParked.row, lastCarParked.spotNumber + 1, lastCarParked.level, None)
        
        if lastCarParked.row < self.rows:
            return ParkingSlot(lastCarParked.row + 1, 0, self.levelNumber, None)
        
    def park(self, vehicle):
        freeParking = self.findAvailableSlots()
        if not freeParking:
            return None

        else:
            freeParking.park(vehicle)
            self.parkingSlots.append(freeParking)
            self.availableSpots -= 1
        

        

