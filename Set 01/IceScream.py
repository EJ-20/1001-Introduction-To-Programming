#Get input from the user

barsInJune = int(input('Enter the number of bars ordered in June: '))
barsInJuly = int(input('Enter the number of bars ordered in July: '))
barsInAugust = int(input('Enter the number of bars ordered in August: '))

#Calculate the number of small and large boxes packed

bars = barsInJune + barsInJuly + barsInAugust
smallBoxes = (bars // 2) // 5
largeBoxes = (bars // 2) // 20

#Calculate the selling price of small and large boxes
totalCost = 0.5 * barsInJune + 1 * barsInJuly + 0.75 * barsInAugust
avgCost = totalCost/bars

smallSP = (avgCost * 0.9 + avgCost) * 5
largeSP = (avgCost * 0.8 + avgCost) * 20

#Print the output

print('Number of small boxes packed: ',smallBoxes)
print('Number of large boxes packed: ',largeBoxes)
print('Selling price per small box: $%4.2f' %smallSP)
print('Selling price per large box: $%5.2f' %largeSP)

