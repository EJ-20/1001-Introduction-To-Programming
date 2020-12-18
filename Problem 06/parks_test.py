from parks import *     #import the class and methods from parks

bigPark = Park("Big Park", "NL", 200, 1950, 5)  
smallPark = Park("Small Park", "ON", 150, 1980, 6)
medPark = Park("Medium Park", "BC", 165, 1992, 10)

#Get information of 3 parks and print
bigPark.parkInfo()
print()
smallPark.parkInfo()
print()
medPark.parkInfo()
print()

#get the entry fee for the park based on the per-day entry fee for the 3 parks
print('Cost for 2 days in Big Park is $%4.2f' % bigPark.getEntryFee(2))
print()
print('Cost for 4 days in Small Park is $%4.2f' % smallPark.getEntryFee(4))
print()
print('Cost for 7 days in Medium Park is $%4.2f' % medPark.getEntryFee(7))

#set a new area for the Big Park
print('Park name: ', bigPark.getName())
bigPark.setArea(400)
print('Updated park area: ', bigPark.getArea())
print()

#Get the total number of parks 
print('The total number of Parks are: ', medPark.getNum())
