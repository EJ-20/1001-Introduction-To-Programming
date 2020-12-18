while True:
    
    #Assign variables
    
    a = ""
    i = 0
    consonants = 0

    #Ask for user input
    
    word = input('Please enter a word or zzz to quit: ').lower()

    #Assign sentinel value
    
    if word == "zzz":
        break
    
    #Check for consonants
    
    while i < len(word):
        letter = word[i]        
    
        if letter == "a":
            letter == "a"
            
        elif letter == "e":
            letter == "e"
            
        elif letter == "i":
            letter == "i"
            
        elif letter == "o":
            letter == "o"
            
        elif letter == "u":
            letter == "u"
            
        else:
            letter = "?"
            consonants += 1
        a = a + letter
        i += 1

    #Print output
        
    print('The original word is: ',word)
    print('The word without consonants is: ',a)
    print('The number of consonants in the word are: ',consonants)
    
