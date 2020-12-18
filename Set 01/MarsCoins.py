#Ask the user for the inputs

numMaruvians = int(input('Please enter the number of Maruvians: '))
numCaruvians = int(input('Please enter the number of Caruvians: '))
numTaruvians = int(input('Please enter the number of Taruvians: '))
numParuvians = int(input('Please enter the number of Paruvians: '))
numFriends = int(input('Please enter the number of friends: '))

#Convert the currency into Maruvian

numParuvians += numTaruvians * 6
numParuvians += numCaruvians * 12
numMaruvians += numParuvians // 24

#Total number of Maruvians

print('Marvin has ', numMaruvians, ' Maruvian(s) in total.')

#Calculate how much his friends receive

amountShared = numMaruvians // (numFriends + 1)
print('He gives ', amountShared, ' Maruvian(s) to himself and to each of his ', numFriends, ' friends.')

#Calculate and print the leftover

leftoverParuvians =  (numParuvians/24 - numParuvians//24) * 24
leftoverMaruvians = numMaruvians - amountShared * (numFriends + 1)

print('Marvin puts ', leftoverMaruvians, 'Maruvian(s) and ', round(leftoverParuvians), ' Paruvian(s) back in the jar')
      
