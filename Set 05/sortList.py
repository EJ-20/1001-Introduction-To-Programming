def findNext(names, index):     #define the function findNext
                            
    smallest = names[index]     #assume the first element is the smallest (alphabetically)

    #get the smallest element in the list 
    for i in range(index, len(names)):  
        check = names[i]
        if check < smallest:
            smallest = check

    #get the index of the smallest element in the list and return
    for smallestIndex in range(len(names)):
        current = names[smallestIndex]
        if current == smallest:
            return smallestIndex
            
def putInOrder(names, index, lowest):   #define the function putInOrder
    names = names

    #change the index and arrange it alphabetically 
    temp = names[index]
    names[index] = names[lowest]
    names[lowest] = temp
    
    return names    #return the updated list 
    
def main():
    
    names = ["Zita", "Henny", "Benny", "Harold", "Danny", "Penny"]      #create a list of names
    
    print('Unsorted list: \n', names)   #print the list of names
    index = 0

    #use findNext and putInOrder to sort the list
    for i in range(len(names)):
        a = findNext(names, index)
        sortedList = putInOrder(names, index, a)
        index += 1

    print('Sorted List: \n', sortedList)    #print the sorted list

main()
