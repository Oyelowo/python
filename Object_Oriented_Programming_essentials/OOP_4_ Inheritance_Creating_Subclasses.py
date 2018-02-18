# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 04:40:58 2018

@author: oyedayo oyelowo
"""

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

        # creating subclass to inherit attributes from another class.

#here the class "Student" is being used as paarameter for Teacher
class Teacher(Student):
    raise_allowance = 1.5
#    if you need to add extra paarameter, you dont have to copy paste all the codes in the body.

    def __init__(self, first, last, allowance, car):
        super().__init__(first, last, allowance)
    # also can be done as below, however, the above is more preferable:
#        Student.__init__(self, first, last, allowance)
        self.car = car  # additional attribute

# creating subclass to inherit attributes from another class.
# class Teacher(Student):
#    pass


class Supervisor(Student):
    def __init__(self, first, last, allowance, students=None):
        super().__init__(first, last, allowance)
        if students == None:
            self.students = []
        else:
            self.students = students

    def add_stud(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    def remove_stud(self, stud):
        if stud in self.students:
            self.students.remove(stud)

            # check number of students a supervisor supervises.
    def print_studs(self):
        for stud in self.students:
            print('------->', stud.fullname())



# Example of usage
stud1 = Student('Oyelowo', 'Oyedayo', 99)
stud2 = Student('Sonja', 'Jackson', 93)
print(stud1.email)
print(stud2.email)

#tch_1= Teacher('Mika', 'Tuomo', 80000, )
#tch_2 = Teacher("Petri", 'Emil', 120000)
# print(tch_1.email)
# print(tch_2.email)

print(help(Teacher))
# here, u can see the method resolution order, when using the class "Teacher", it first
# searches throught the Teacher method,
# if it does not find there, it searches through, Student class, the the builtins.ojects


# tch_1.allowance
# tch_1.apply_raise()
# tch_1.allowance

# however, if one needs tochange any of the attributes e.g the raise_allowance, then it canbe
# done in the subclass.(check above)

# NOTE: changes in the subclass does not alter the parent class.


# Test the extra attribute - car
tch_1 = Teacher('Mika', 'Tuomo', 80000, 'Toyota')
tch_2 = Teacher("Petri", 'Emil', 120000, 'Volvo')
print(tch_1.car)
print(tch_2.car)

tch_1.allowance
tch_1.apply_raise()
tch_1.allowance

super1 = Supervisor('king', 'Wood', 403000, [stud1])
super1.email


super1.print_studs()
super1.add_stud(stud2)
super1.print_studs()
super1.remove_stud(stud2)

# isinstance() is an inbuilt function which tells if an object is an instance of a class
print(isinstance(super1, Student))
print(isinstance(super1, Teacher))

print(issubclass(Supervisor, Student))
print(issubclass(Supervisor, Teacher))


