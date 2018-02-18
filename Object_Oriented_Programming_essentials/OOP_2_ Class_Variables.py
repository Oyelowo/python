# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:59:16 2018

@author: Oyedayo Oyelowo
"""

#class variables are varibales that are share amongst members of a class
#while instances can be unique. class variables should be thesame for each instance.


# Python Object-Oriented Programming
#create simple classes.
#
#initialise simple classes attribute and create methods
class Student:
#    class variable
    raise_grade=1.08
    num_of_students=0
    
    #initialise(like constructor in java)
    def __init__(self, first, last, grade):
#        create instance variables
        self.firstname =first
        self.lastname = last
        self.grade = grade
        #email can be created from name
        self.email = '{0}.{1}@helsinki.fi'.format(first, last).lower()
        
#        Here, I use Student rather than self because it's a constant value that can be
        #overwritten, as the number of Students applies to all. I use it under __init__
        #because it runs everytime I use the class on a new student object.
        
        Student.num_of_students +=1
        
    #here, self has to be used as the parameter to make it function.
    def fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)
    
    def apply_raise(self):
        #class variable can be accessed via the class name itself or an instance of the class
        #self gives the ability to change the value for the single instance if need be.
        #e.g if I increase the raise_grade of student 1 alone, it does not affect other students,
        #like the class name(Student) will.
        self.grade= int(self.grade* self.raise_grade)
#        self.grade= int(self.grade* Student.raise_grade)

#   This is not an optimal practice
#    def apply_raise(self):
#        self.grade= int(self.grade* 1.08)
        
#Example of usage
stud1 = Student('Oyelowo', 'Oyedayo', 99)
stud2 = Student('Sonja','mari', 93)
stud3 = Student(first='muna',last='skii', grade=4.2)

#check ther attributes
#stud1.__dict__
#Student.__dict__


#using the apply_raise function. The advantage of using "self" instead of class
#name "Student" in the apply_raise function is that, I can alter a specific object, rather
#than using the universal variable..
print(stud1.grade)
stud1.raise_grade=2
Student.apply_raise(stud1) 
print(stud1.grade)

#here, student 2 object uses the universal class variable value i.e"raise_grade"
print(stud2.grade)
Student.apply_raise(stud2) 
print(stud2.grade)


stud1.__dict__
stud2.__dict__

#here, when you try to access an attribute on an instance, it first checks if 
#the instance contains the attribute and if it does not, it checks if class it inherits from
#contains that attribute.
print(Student.raise_grade)
print(stud1.raise_grade)
print(stud2.raise_grade)


#change raise amount for the class and instances
Student.raise_grade=1.09
print(Student.raise_grade)
print(stud1.raise_grade)
print(stud2.raise_grade)


#if you change the raise amount for each of the student, it does not affect others
#but changes that of the student alone.
stud1.raise_grade=1.11
print(Student.raise_grade)
print(stud1.raise_grade)
print(stud2.raise_grade)

#check the raise amount for the specifit object.
print(stud1.__dict__)

#check the number of students now.
print(Student.num_of_students)

