#Ask for the weight limit of truck
truckLimit = int(input('Please enter the weight limit of the truck: '))
print()

#Declare variables
i = 0
north = 0
south = 0
east = 0
west = 0

#Start loop
while True:

    #Ask for the weight of a package
    weight = float(input('Please enter the weight of a package: '))
    
    i += weight

    #Assign the sentinel value
    if i >= truckLimit:
        break

    #Ask for package ID
    packageID = int(input('Please enter the package ID number: '))

    #Ask for zone
    zone = input('Please enter the zone: ')

    #Calculate how many packages in each zone
    if zone == "East":
        east += 1
    if zone == "North":
        north += 1
    if zone == "South":
        south += 1
    if zone == "West":
        west += 1

    #Print the information about the package
    print()
    print('The following package is on the truck: ')
    print("Pkg No. = ", packageID, ", Zone = ", zone, ", Pkg Wgt = ", weight)
    print()

#Calculate the total number of packages
total = north + south + east + west

#Print the output
print(north, " packages are on the truck for North zone")
print(south, " packages are on the truck for South zone")
print(east, " packages are on the truck for East zone")
print(west, " packages are on the truck for West zone")
print()
print(total, " packages are loaded on the truck")
