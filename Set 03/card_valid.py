def main(): #Define main
    
    cardNum = int(input("Please enter your card number: ")) #Get card number from user
    if isValid(cardNum): #Call the function isValid to check if the card number is valid
        print("The number, ", cardNum, ", is valid") #Print the output
    else:
        print("The number, ", cardNum, ", is invalid") #Print the output

def isValid(number): #Define the function isValid
    
    #Return True only if it meets the necessary conditions
    if checkIfDivisible(number) == True and getSize(number) >= 13 and getSize(number)<= 16 and isPrefix(number) == True:
        return True
    
    else:
        return False

def sumDoubleEvenLocation(number):  #Define the function sumDoubleEvenLocation

    #Declare the variables
    b = 0
    z = str(number) 
                    
    k = z[-2::-2] #extract the numbers in the even location of the string

    #Double the value and sum it
    for x in k:
        x = int(x)
        a = x*2

        #if the double is of 2 digits, split the values and add them
        if a >= 10:
            c = a// 10
            d = a % 10
            a = c + d
        b += a

    #Return the result
    return b
    
def getDigit(number): #Define the function getDigit
                    
    z = str(number) #convert the argument to string

    k = z[-2::-2] #Extract the numbers from the even locations of the string
    
    for x in k:
        
        x = int(x)
        a = x*2

        #if the double is of 2 digits, split the values and add them
        if a >= 10:
            c = a// 10
            d = a % 10
            a = c + d

    return a
    

def sumOddLocation(number): #define the function sumOddLocation

    #Assign variables
    z = str(number)
    b = 0   
    
    k = z[::-2] #Extract the numbers from the odd locations of the string

    #Add the numbers
    for x in k:
        x = int(x)    
        b += x

    #Return the result
    return b

def isPrefix(number): #Define the variable isPrefix
                    
    x = str(number) #Convert the argument to string
                                                                                        
    if x[0] == '4' or x[0] == '5' or x[0] == '6' or x[0] == '3' and x[1] == '7':    #Check if it meets the necessary conditions

        #Return the results
        return True
    else:
        return False

def getSize(d): #Define the function getSize
    
    #Use length function to get the length of the string
    d = str(d)
    x = len(d)
                
    return x #Return the result

def checkIfDivisible(number): #Define the function checkIfDivisible

    #add the two numbers from the two functions
    a = sumOddLocation(number) + sumDoubleEvenLocation(number)

    #Check if they meet the necessary conditions and return the value
    if a % 10 == 0:
        return True
    else:
        return False

def getPrefix(number, k): #Define the function getPrefix

	number = str(number)
	a = ''
	if len(number) < k:
		return number
	else:
		while i <= k:
			a += number[i]
			i += 1
		
main()
