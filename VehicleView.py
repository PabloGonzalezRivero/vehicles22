from ControllerVehicle import ControllerVehicle
from vehicleapi import getDistance 

controler = ControllerVehicle()

def checkPlate():
    plate =""
    while True:
        plate=input("Enter the new car's plate :" )
        if(len(plate) == 7):
            numPart = plate[0:4]
            lettersPart = plate[4:]
            if(numPart.isdigit()):
                if(lettersPart.isalpha()):
                    break
        print("Error with the plate entry")
    return plate

def addVehicle():
    
    
    while True:
        plate=checkPlate()
        desc =input("Enter Description: ")
        chasis=input("Enter the new car's chasis (17 characters needed): ")
        if(len(chasis)==17):
            break
        print("Error entering the chasis (17 characters needed)")
    driver=input("Enter the name of the driver of the new car: ")
    if (controler.addVehicle(plate,desc,chasis,driver)):
        print("Vehicle added successfully")
    else:
        print("Error adding the vehicle")

def delVehicle():
    plate = checkPlate()
    if controler.delVehicle(plate):
        print("Vehicle deleted successfully")
    else:
        print("Error deleting the vehicle")

def addOdometer():
        plate=checkPlate()
        date = input("Enter the date (dd/mm/YYYY): ")
        source=input("Enter the source: ")
        dest=input("Enter the destination: ")
        kms = getDistance(source,dest)/100
        if(controler.addOdometer(plate,date,source,dest,kms)):
            print("Odometer added succesfully")
        else:
            print("Error. The odometer couldn't be added")

def confirmOdometer():
    plate=checkPlate()
    date = input("Enter the date (dd/mm/YYYY): ")
    if controler.checkOdometer(plate,date):
        print("Odometer confirmed")
    else:
        print("Error. The odometer couldn't be confirmed")

def listVehicles():
    if(count < 0):
        print("There are no vehicles yet")
    else:
        vehicles = controler.getVehicles()
        for plate,vehicle in vehicles.items():
            print("Plate: ",plate)
            print("Descripton: ",vehicle.getDescription())
            print("Driver: ",vehicle.getDriver())
            print("Chasis: ",vehicle.getChasis())
            print("Unconfirmed odometer")
            for date,odometer in vehicle.getOdometer().items():
                print("\t",date,odometer[0],odometer[1],odometer[2])

while True:  
    count = controler.countVehicles()  
    print("Currently there are ",count," vehicles registred.")
    print("1.- Add a vehicle")
    print("2.- Delete vehicle")
    print("3.- Add odometer")
    print("4.- Confirm odometer")
    print("5.- List vehicle")
    print("6.- Exit")
    option = int(input("Choose option: "))
    if(option == 6):
        print("BYE")
        break
    elif (option == 1):
        addVehicle()
    elif (option == 2):
        delVehicle()
    elif (option == 3):
        addOdometer()
    elif (option == 4):
        confirmOdometer()
    elif (option == 5):
        listVehicles()
    else:
        print("Option error")

