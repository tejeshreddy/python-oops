from abc import ABCMeta, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 1
    LARGE = 2
    TRUCK = 5


class Vehicle(metaclass=ABCMeta):
    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []
    
    def park_vehicle(self, spot):
        self.spots_taken.append(spot)

    def remove_vehicle(self):
        self.spots_taken.
    
    @abstractmethod
    def can_fit_in_spot(self):
        pass



    
