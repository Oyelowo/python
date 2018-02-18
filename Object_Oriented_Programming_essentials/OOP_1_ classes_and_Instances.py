# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:58:07 2018

@author: oyedayo Oyelowo
"""

# Python Object-Oriented Programming
#create simple classes.
#
#initialise simple classes attribute and create methods

class Student:
    #initialise(like constructor in java)
    def __init__(self, first, last, grade):
#        create instance variables
        self.firstname =first
        self.lastname = last
        self.grade = grade
        #email can be created from name
        self.email = '{0}.{1}@helsinki.fi'.format(first, last).lower()
        #        can also be or use strings concatenation:
#        self.email = '{firstname}.{lastname}@helsinki.fi'.format(firstname=first, lastname=last)
#        self.email= first + '.' + last + '@helsinki.fi'
    
    #here, self has to be used as the parameter to make it function.
    def fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)
        
#Example of usage
stud1 = Student('Oyelowo', 'Oyedayo', 99)
stud2 = Student('Sonja','mari')
stud3 = Student(first='muna',last='skii', grade=4.2)

#print(stud1)
#print(stud2)

stud1.fullname()
Student.fullname(stud1)

print(stud2.fullname())

print(stud3.fullname())

