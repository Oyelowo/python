# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 02:53:43 2018

@author: Oyedayo Oyelowo
"""

#difference between regular methods, class methods and static methods:
#regular methods in a class automatically take instances as their first argument
#and by convention is called self.

##########################################################################################
######################CLASS METHOD###################################################### 
#To change a regular method to a class method, You can add a decorato#e.g "@classmethod.
#with this, it can take the class as the first argument.

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
        
#        Here, I use Student rather than self because I constant value that can be
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
       
        #decorator which can be used to alter the functionality of a method.
        #for regular method, common convention is self while for class method, it
        #is "cls". You can't use the word "Class" here because it means something else in 
        #the language, which is a keyword that was used to create new class.
        #here, I am working with the class instead of instances
    @classmethod
    def set_raise_score(cls, score):
        cls.raise_grade= score
        
#        Class methods can also be used as alternative constructive.
    #this will be used as alternative constructor to avoid repetition when creating new students
    @classmethod
    def from_String(cls, stud_str):
        firstname, lastname, grade =stud_str.split('-') 
        return cls(firstname, lastname, int(grade))
    
#    another decorator but static method
#        if you dont access the class anywhere in the function, then, it should be static.
    @staticmethod
    def is_schoolday(day):
        #here I used 5 and 6 because the datetime module starts counting the day of
        #the week at 0 till 6. so, saturday and sunday would be 5 and 6 respectively.
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True

        
#Example of usage
stud1 = Student('Oyelowo', 'Oyedayo', 99)
stud2 = Student('Sonja','Jackson', 93)
stud3 = Student(first='muna',last='skii', grade=4.2)

#check ther attributes
#stud1.__dict__
#Student.__dict__

print(Student.raise_grade)
print(stud1.raise_grade)
print(stud2.raise_grade)

#it automatically accepts the class and no need to parse it in
Student.set_raise_score(1.4)

#this is same as below, but now using class to effect this:
#Student.raise_grade= 1.4

print(Student.raise_grade)
print(stud1.raise_grade)
print(stud2.raise_grade)

#here, the  value changed because the class method worked with the class rather
#than the instances.

#class methods can also be run from instances but not really sensible. e.g
stud1.set_raise_score(1.6)
#you see, here, it also changes the class variable which changes the values for 
#other objects(students) as well and this could create confusion.


#class methods can also be used as alternative constructors. i.e you can use
#it to provide multiple ways of creating objects.

stud_str_1 = 'Lowo-Blayz-1000000'
stud_str_2 = 'Lionel-Ronaldo-800000'
stud_str_3 = 'Christiano_-evez-300000'

#if I want to create a new student:
firstname, lastname, grade =stud_str_1.split('-') 
new_Stud_1 = Student(firstname, lastname, grade)
print(new_Stud_1.email)
print(new_Stud_1.grade)
#instead of the above, an alternative class constructor has been created

#now, you can see 
new_stud_1 = Student.from_String(stud_str_1)
print(new_stud_1.email)
print(new_stud_1.grade)
new_stud_1.lastname

new_stud_2 = Student.from_String(stud_str_2)
print(new_stud_2.email)
print(new_stud_2.grade)

new_stud_3 = Student.from_String(stud_str_3)
print(new_stud_3.email)
print(new_stud_3.grade)



Student.apply_raise(new_stud_3)
new_stud_3.grade
new_stud_3.raise_grade=20
new_stud_3.__dict__

Student.apply_raise(new_stud_3)
new_stud_3.grade


###############################################################################
############STATIC METHOD######################################################
#While regular methods pass first argument as self and class methdo passes first
#argument as cls, static methods don't automatically a pass anything. They dont pass the
#instance or the class. we include them in our class becuase they have logical  
#connection with the class.
#e.g take a date and tell if it is a working date or not. This does not have a 
#specific connection with the class.

import datetime
mydate= datetime.date(2018, 2, 6)
mydate.weekday()
print(Student.is_schoolday(mydate))
