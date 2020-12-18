class Course:   #define the class "Course"
    def __init__(self, title, ID):  #define the initializer and set the instance variables 
        self.__title = title
        self.__ID = ID

    def getTitle(self):     #define getTitle that returns the title
        return self.__title
    def getID(self):        #define getID that returns the ID
        return self.__ID

    def display(self):      #define the display method that prints the information 
        return "Title: " + str(self.getTitle()) + "\nID: " + str(self.getID())
        
class OfferedCourse(Course):    #define the class "OfferedCourse" which inherits properties from the "Course" class
    def __init__(self, title, ID):      #define the initializer method and set the instance variables
        super().__init__(title, ID)
        self.__enrolled = [] 

    def getEnrolled(self):      #define getEnrolled that returns the number of students enrolled
        x = str(len(self.__enrolled))   
        return x

    def addStudent(self, ID):   #define addStudent that adds student's ID into the list if the student is not enrolled already
        if ID in self.__enrolled:
            return 
        else:
            self.__enrolled.append(ID)
            
    def dropStudent(self, ID):  #define drop student that removes a student from the list of enrolled students if he/she is enrolled
        if ID in self.__enrolled:
            self.__enrolled.remove(ID)
        else:
            return

    def display(self, enrolled):   #define the display method that prints the course name, ID and the number of students enrolled
        super().display()
        print("Enrolment: " + enrolled)
    
class StudentCourse(Course):        #define the class "StudentCourse" which inherits properties of the class "Course"
    def __init__(self, title, ID, grade):   #define the initializer method and set the instance variables
        super().__init__(title, ID)
        self.__grade = grade

    def getGrade(self):         #define getGrade that returns the grade
        return self.__grade

    def display(self, x):       #define the display method that prints the course name, ID and the grade obtained by the student
        super().display() + " " +"Grade: " + x
    

def main():         #define the main method
    #set values for name, ID and grade
    name = "Intro to programming"   
    ID = 83713
    grade = 83

    #call the classes and display the output
    x = Course(name, ID)
    a = OfferedCourse(name, ID)
    a.addStudent(2392)
    a.addStudent(2939)
    a.addStudent(2939)
    a.addStudent(2990)
    total = a.getEnrolled()
    a.display(total)
    b = StudentCourse(name, ID, grade)
    b.display(grade)
    
main()

    
        
