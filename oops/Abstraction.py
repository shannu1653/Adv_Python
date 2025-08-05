#Abstraction : It is a phenomenon of hiding unncecessary details to the user and allows him to 

from abc import ABC, abstractmethod

class WaterFilter(ABC):
    @abstractmethod
    def waterPasser(self):
        pass

class ColdWater(WaterFilter):
    def waterPasser(self):
        print("Cold water served")
    
class HotWater(WaterFilter):
    def waterPasser(self):
        print("Hot water served")

class NormalWater(WaterFilter):
    def waterPasser(self):
        print("Normal water served")

c=ColdWater()
h=HotWater()
n=NormalWater()

c.waterPasser()
h.waterPasser()
n.waterPasser()

#ex2 vahicles

from abc import ABC, abstractmethod

class Vehicles(ABC):
    @abstractmethod
    def vehiclepass(self):
        pass

class Truck(Vehicles):
    def vehiclepass(self):
        print("Truck")
    
class Auto(Vehicles):
    def vehiclepass(self):
        print("Auto")

class bike(Vehicles):
    def vehiclepass(self):
        print("Bike")

t=Truck()
a=Auto()
b=bike()

t.vehiclepass()
a.vehiclepass()
b.vehiclepass()