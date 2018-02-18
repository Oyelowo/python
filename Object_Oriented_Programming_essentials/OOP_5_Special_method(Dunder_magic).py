# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:59:44 2018

@author: oyeda
"""
#######################################
###SPECIAL_METHODS###########
#allows the emulation of some built-in behaviours within python
#It is also used to implement operator overloading


# Inheritance enables us to inherit attributes from parent class
# you can add new functionality without affecting the parent class in anyway

# difference between regular methods, class methods and static methods:
# regular methods in a class automatically take instances as their first argument
# and by convention is called self.

##########################################################################################
######################CLASS METHOD######################################################
# To change a regular method to a class method, You can add a decorato#e.g "@classmethod.
# with this, it can take the class as the first argument.

# initialise simple classes attribute and create methods


class Student:
    #    class variable
    raise_allowance = 1.08
    num_of_students = 0

    # initialise(like constructor in java)
    def __init__(self, first, last, allowance):
        #        create instance variables
        self.firstname = first
        self.lastname = last
        self.allowance = allowance
        # email can be created from name
        self.email = '{0}.{1}@helsinki.fi'.format(first, last).lower()

#        Here, I use Student rather than self because I constant value that can be
        # overwritten, as the number of Students applies to all. I use it under __init__
        # because it runs everytime I use the class on a new student object.

        Student.num_of_students += 1

    # here, self has to be used as the parameter to make it function.
    def fullname(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        # class variable can be accessed via the class name itself or an instance of the class
        # self gives the ability to change the value for the single instance if need be.
        # e.g if I increase the raise_grade of student 1 alone, it does not affect other students,
        # like the class name(Student) will.
        self.allowance = int(self.allowance * self.raise_allowance)
#        self.grade= int(self.grade* Student.raise_grade)
        
#        it's good to always have __repr__ together with __str__
    def __repr__(self):
#        use something that can be used to recreate the employee
        return "Employee('{}', '{}', '{}')".format(self.firstname, self.lastname, self.allowance)
    
    def __str__(self):
        return "'{}' - '{}'".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.allowance + other.allowance
    
    def __len__(self):
        return len(self.fullname())

  


# Example of usage
stud1 = Student('Oyelowo', 'Oyedayo', 99)
stud2 = Student('Sonja', 'Jackson', 93)
print(stud1.email)

#The built_in methods are always separated by double underscore(__) aka dunder
#This include __init__(self), __repr__(self)   __str__(self)
#__repr__ is an unambiguous representation of the object and should be used for
#debugging. should be seen by developers.
#__str__ is more of a readable user object and is meant to be used as a display
#to the end user
#can be used for printing out vague student object
stud1
#e.g, the above appears as " <__main__.Student at 0x1c8119750f0>" when printed

#after including the __repr__ in the class and rerunning it, i got the below
#"Employee('Oyelowo', 'Oyedayo', '99')"

print(stud1)
#again, after reruning with the __str__, i got the below:
#'Oyelowo Oyedayo' - 'oyelowo.oyedayo@helsinki.fi'

#the above two can also be derived by using the below:
print(repr(stud1))
print(str(stud1))

#in the background, it is directly calling those special methods.

#another way to show these.
#e.g
print(stud1.__repr__())
print(stud1.__str__())

#overall, they help to change how our objects are displayed

#there are also a lot of special methods for arithmetic
print(1+4)
#this is using a special method in the background called __add__
#this can be access directly as
print(int.__add__(1,4))
#this gives thesame result.

#strings use their own dunder for concatenation.
print("oye" + "lowo")
#also as
print(str.__add__("oye","lowo"))

#another example has been added as a method "__add" in the class. 
#this is just for hypothetical example. would be better in real world to be
#be explicit about such operation.

#e.g
print(stud1 +  stud2)
#this was made possible with the __add__ method above. if it is deleted out, it will
#result in an error not supporting such operation.


#len function is also a special dunder method
print(len('oyelowo'))
print('oyelowo'.__len__())

#the method __len__ was created to make the below possible
print(len(stud1))

#there are many other special dunder methods.


####EXTRA:
#return NotImplemented is a way of falling back on other objects if they can 
#handle the operation and if they cannot, it will eventually return an error.
#this can be found in the datetime module.
