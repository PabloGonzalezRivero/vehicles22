from vehicle import Vehicle
from datetime import datetime



class ControllerVehicle():

    def __init__(self):
        self._vehicles = {} # Key -> Plate, Value --> Vehicle

    def addVehicle(self,plate,description,chasis,driver):
        if plate in self._vehicles:
            return False
        newVehicle = Vehicle(plate,description,chasis,driver)
        self._vehicles[plate] = newVehicle
        return True

    def delVehicle(self,plate):
        if plate not in self._vehicles:
            return False
        self._vehicles.pop(plate) # del self._vehicles[plate]
        return True
    
    def countVehicles(self):
        count=0
        for i in range(len(self._vehicles)):
            count=count +1
        return count

    def addOdometer(self,plate,date,source,dest,kms):
        if plate not in self._vehicles:
            return False
        vehicle=self._vehicles[plate]
        vehicle.addOdometer(date,source,dest,kms)
        return True
    
    def getVehicles(self):
        return self._vehicles
    
    def checkOdometer(self,plate,date):
        if plate not in self._vehicles:
            return False
        vehicle=self._vehicles[plate]
        if date not in vehicle.getOdometer():
            return False
        else:
            vehicle.confirmOdometer(date)
            return True
             
