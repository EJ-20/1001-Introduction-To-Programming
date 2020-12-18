class Park:         #define the class Park
    noOfParks = 1   #declare the variable noOfParks to count the number of parks
    def __init__(self, name, location, area, year, fee):    #define the initializer method

        #set values to the instance variables
        self.__num = type(self).noOfParks
        self.__name = name
        self.__location = location
        self.__area = area
        self.__year = year
        self.__fee = fee
        type(self).noOfParks += 1   #increment the noOfParks variable by 1 

    def setArea(self, newArea):     #define the mutator method that changes the value of the area
        self.__area = newArea

    #define the accessor methods for each instance variable
    def getName(self):
        return self.__name
    def getLocation(self):
        return self.__location
    def getArea(self):
        return self.__area
    def getYear(self):
        return self.__year
    def getFee(self):
        return self.__fee

    def getEntryFee(self, days):
        return self.__fee*days

    def getNum(self):
        return self.__num

    #define the special method to print the information about the park
    def __str__(self):
        print( "Name: " + self.__name +\
               "\nLocation: " , self.__location +\
               '\nArea covered (km^2): ' + str(self.__area) +\
               '\nYear established: ' + str(self.__year)+\
               '\nEntry fee per day: $' + str(self.__fee))
        print(self.getEntryFee(3))

    def parkInfo(self):     #define parkInfo that returns the info about the park
        return self.__str__()

