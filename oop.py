# OOP = Object Oriented Programming
# We create objects that don' exist but come from classes and objects.
# It always has classes and objects/instances
# Methods are items of the class
# Objects are found within a class
# An object takes on properties of the class.

# SYNTAX OF OOP.
# 1. Creating a class.
# Cohort class 
# Add a constructer for the cohort class
# create a function or method to the class that prints the cohort name and the total number of students.
# create a new instance or object of the cohort class.

# SOLUTION
class cohort:
     def __init__(self, cohortName, numberOfStudents):
        self.cohortName = cohortName 
        self.numberOfStudents = numberOfStudents
        
cohortOne = cohort('Cohort1', 67)
print(cohortOne.cohortName)

# b)
class cohort:
    def __init__(self, cohortName, numberOfStudents):
        self.cohortName = cohortName 
        self.numberOfStudents = numberOfStudents

    def year(self):
      print(f"The cohort name is {self.cohortName} of {self.numberOfStudents} students")
      
cohortClass = cohort('Cohort1', 67)
cohortClass.year()

# c)
class cohort:
    def __init__(self, cohortName, numberOfStudents, studentName, regNo, studentNumber, age):
        self.cohortName = cohortName 
        self.numberOfStudents = numberOfStudents
        self.studentName = studentName
        self.regNo = regNo
        self.studentNumber = studentNumber
        self.age = age
        
cohortClass = cohort('CohortIV', 56, 'Madrine Denla', '2024/DSC/0083/SS', 2244118, 21)
print(cohortClass.cohortName)
print(cohortClass.numberOfStudents)
print(cohortClass.regNo)
print(cohortClass.studentName)
print(cohortClass.studentNumber)
print(cohortClass.age)

