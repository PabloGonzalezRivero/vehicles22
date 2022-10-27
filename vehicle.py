class Vehicle:
    def __init__(self,plate,desc,chasis,dn):
        self.__plate = plate
        self.__desc = desc
        self.__chasis = chasis
        self.__dn = dn
        self.__od = {}
        self.__kms = 0
        self.__h = ""

    def getPlate(self):
        return self.__plate

    def getDescription(self):
        return self.__desc

    def getChasis(self):
        return self.__chasis

    def getDriver(self):
        return self.__dn  
    
    def getOdometer(self):
        return self.__od

    def getKilometers(self):
        return self.__kms

    def getHistory(self):
        return self.__h

    def addOdometer(self,date,source,dest,kms):
        self.__od[date]= (source,dest,kms)

    def confirmOdometer(self,date):
        details = self.__od.pop(date)
        self.__h += str(details[0]) + "-" + str(details[1]) + "-" + str(details[2]) + "\n"
        self.__kms += details[2]
    