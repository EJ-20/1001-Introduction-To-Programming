#Define the main funtion 
def main():
    
    #Initiate loop
    while True:
        
        #Get user input
        num = input("Enter a string of digits or 'quit' to stop: ")

        if num == "quit": #Set sentinel value 
            break

        processStr(num) #Call the processStr function to get sum and product
        print('The highest digit in the given string is: ', getHighest(num)) #Get the highest number from the getHighest function
        print(getHasRepeatDigit(num)) #Check if numbers are repeated by calling getHasRepeatDigit funtion

#Define the processStr funtion
def processStr(x):

    #Declare variables
    sum = 0
    product = 1

    #Calculate sum and product
    for i in x:
        i = int(i)
        sum += i
        product *= i

    #Print the sum and product
    print('The sum of the digits in ', x,' is ', sum)
    print('The product of the digits in ', x, ' is ', product)

#Define the getHighest funtion
def getHighest(y):

    #Declare the variables
    i = 0
    b = ''

    #Extract the highest value in the string 
    while i < len(y):
        a = y[i]
  
        for j in y:

            if j > a:
                b = j
        i += 1

    #Return the highest value
    return b 

#Define the getHasRepeatDigit funtion
def getHasRepeatDigit(z):

    #Declare the variables
    i = 0
    x = 0

    #Check if any number is repeated
    while i < len(z):
        
        a = z[i]
        
        for k in z:
            
            if k == a:
                x += 1
        i += 1

    #Return the restult
    if x > len(z):
            
        return "The string has repeated digits."
    else:
        return "The string has no repeated digits."

#Call main
main()
