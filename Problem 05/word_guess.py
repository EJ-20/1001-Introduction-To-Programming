from random import randint

#Create a list of words
wordList = ["task", "orange", "suspect", "meeting", "vote", "emergency", "vent"]

#set the initial value to yes
next = 'y'
while next == 'y':
    
    wrong = 0   #declared variable 'wrong' to count the number of letters that aren't in the word
    randomNum = randint(0,len(wordList)-1)  #generates a random number to get a random word from the list
    word = wordList[randomNum]  #gets a random word from the list 

    list = ['*' for x in word]  #create a list of asterisk with the length of the word generated
    
    i = 0
    count = 0
    while count < len(word):
        
        letter = input("Guess a letter in the word >")  #Ask the user to guess a letter
        
        if letter in list:  #Check if the letter is repeated
                print('Letter already entered, enter a different letter')
                continue
        x = 0
        found = False
        while x < len(word):    
            
            if letter == word[x]:   #check if the letter is in the word
                found = True
            
                count += 1  #count the number of letters right 
                list.pop(x)
                list.insert(x, letter)  
            x += 1
            
        
        if not found:
            print(letter, ' is not in word')
            wrong += 1
        for t in range(len(list)):
            print(list[t],end='')   #print the result
        print()
    print('The word is ', word, '. You missed', wrong, 'times')     #print the number of times a wrong letter was input
    next = input('Do you want to guess for another word? Enter y or n >')   #ask if the user wants to repeat the process
print('Finished')
