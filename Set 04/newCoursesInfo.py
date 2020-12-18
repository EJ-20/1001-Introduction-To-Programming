from random import randint    #import the randint function to generate random integers


def initializeMarks(numC, numS): #define the function initializeMarks
     marks = []     #create an empty list to store marks
     i = 0

     #add random integers for each students in the marks list
     while i< numC:
          marks.append([])
          x = 0
          while x < numS:
               a = randint(0,100)
               marks[i].append(a)
               x+= 1
          i += 1
     
     return marks   #return marks
     
        
def computeAllRanges(courses, marks):   #define the function computeAllRanges
     
     x = 0
     print('Courses', end= '   Range of marks')
     print()

     #find the range of courses and print 
     while x < len(courses):
          max = findMaxForRow(marks,x)
          min = findMinForRow(marks,x)
          printRangeForCourse(courses, x, max, min)
          x += 1
          
     
def findMinForRow(marks, row):     #define the function findMinForRow
               
     smallest = marks[row][0]      #assume the first value to be the smallest

     #if a smaller value is found in the list, change the value of smallest
     for t in marks[row]:
          if t < smallest:
                    smallest = t
       
     return smallest     #Return the smallest value in the list

def findMaxForRow(marks, row):     #define the function findMaxForRow
                              
     largest = marks[row][0]  #assume the first value to be the largest

     #if a larger value is found in the list, change the value of largest
     for t in marks[row]:
          if t > largest:
               largest = t
         
     return largest      #return the largest value in the list

def printRangeForCourse(courses, position, max, min):       #define the function printRangeForCourse
                         
     range = max - min   #find the range of the values in the list
     print(courses[position], end= '           %d'%range)   #print the range of the list
     print()
          
               
def computeAllAverages(students, marks):     #define the function computeAllAverages
     
     i = 0
     
     
     print('Student Name', end= '   Average Marks')
     print()

     #get the average marks for each of the students
     while i < len(students):
          x = 0
          avg = 0
          sum = 0
          while x < len(marks):
               sum += marks[x][i]
               x += 1
               
          avg = sum/x
          
          print(students[i], end = '             %4.1f' %avg)    #print the average along with the student name
          print()
          i += 1

def main():    #define the main function

     #make a list of the courses and the students
     courses = ['CS101', 'CS105', 'CS110', 'CS115', 'CS120']
     students = ['Mimmy', 'Timmy', 'Jimmy', 'Pimmy', 'Kimmy', 'Himmy']

     #find the number of courses and students
     numC = 0
     numS = 0
     for i in courses:
          numC += 1

     for x in students:
          numS += 1
     
     marks = initializeMarks(numC, numS)     #get the list of marks from the initializeMarks function
     
     computeAllRanges(courses, marks)   #get the range of marks in each course from the computeAllRanges function
     print()
     computeAllAverages(students, marks)     #get the average marks of each student form the computeAllAverages function
    
main()
