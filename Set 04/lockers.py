Closed = False  #Set the boolean value of closed to False
Open = True #Set the boolean value of open to True
open = []   #Create an empty list to record the lockers that are open

lockers = [Closed for i in range(100)]  #Create a list of 100 closed lockers 

student = 1

#Open the locker if it's closed and vice versa
while student <= 100:
    locker = student
    
    while locker <= 100:
        if lockers[locker-1] == Closed:
            lockers[locker-1] = Open          
        else:
            lockers[locker-1] = Closed
        
        locker += student
        
    student += 1

#Add the lockers that are open in the list
x = 0   
for i in lockers:
    x += 1
    if i == Open:
        
        open.append('L%d'%x)
    
print(open) #print the lockers that are open
