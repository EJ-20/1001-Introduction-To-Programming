from math import sqrt #Import the sqrt function to be used in calculations

def isPrime(number): #define the isPrime function

    #Assign the variables
    x = True
    i = 1

    #Check if the number is prime
    while i <= sqrt(number):
        i += 1
        if i == number:
            continue
        a = number % i
        
        if a  == 0:
            x = False
        
    return x #Return the result
            

def isPlaindrome(number): #define the isPlaindrome function

    #Check if the number is equal to it's reverse and return the result
    if number == reverse(number):
        return True
    else:
        return False
    
def reverse(number): #define the reverse function
    
    number = str(number) #convert the number to string
    
    rev = number[::-1]  #reverse the number
    
    rev = int(rev)  #convert the number to int
    
    return rev #return the number
        
def main(): #define the main function
    
    num = int(input("How many palindromic primes should be computed?: ")) #ask the user for the number of prime and plaindrome numbers they want

    #Assign variables
    x = 0
    i = 0
    y = 2

    #Check if the necessary conditions are met and print the numbers
    while x < num:
        
        if isPrime(y) and isPlaindrome(y):

            #make sure only 10 numbers are printed in a line
            print(reverse(y), end = ' ')
            x += 1
            i += 1
            if i == 10:
                print()
                i = 0
        y += 1
        
    
main() #call main function
