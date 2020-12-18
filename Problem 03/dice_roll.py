#import randint to generate random numbers
from random import randint

#get input from user
rolls = int(input("How many times should we roll the dice? "))

#declare variables
even = 0
odd = 0

#start loop
for i in range(1, rolls+1):

    #generate 2 random numbers
    first = randint(1,6)
    second = randint(1,6)

    #calculate total
    total = first + second

    #print the numbers and their total
    print("You rolled ",first," + ",second, " = ",total)

    #calculate how many even and odd numbers
    if total%2 == 0:
        even += 1
    else:
        odd += 1

#calculate percentage of even and odd
percentEven = (even*100)/rolls
percentOdd = (odd*100)/rolls

#print the output with appropriate string formatting 
print('An even value was rolled %5.2f' %percentEven, '% of the time')
print('An odd value was rolled %5.2f' %percentOdd, '% of the time')
