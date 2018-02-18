# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:43:01 2018

@author: oyeda
"""

#this allows us to give our class attributes getters, ,setters and deleters functionalities.
class Student:
    #    class variable
    raise_allowance = 1.08
    num_of_students = 0

    # initialise(like constructor in java)
    def __init__(self, first, last):
        #        create instance variables
        self.first = first
        self.last = last
        # email can be created from name
        self.email = '{0}.{1}@helsinki.fi'.format(first, last).lower()

#        Here, I use Student rather than self because I constant value that can be
        # overwritten, as the number of Students applies to all. I use it under __init__
        # because it runs everytime I use the class on a new student object.

        Student.num_of_students += 1

    # here, self has to be used as the parameter to make it function.
    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)
    
stud1=Student('Oyedayo', 'Oyelowo')

print(stud1.first)
print(stud1.email)
print(stud1.fullname())


#if you change the firstname, it wont reflect in the email because the email 
#was created out of the first and second name. it does not update automatically.example below:
stud1.first = 'jaga'
print(stud1.first)
print(stud1.email)
print(stud1.fullname())

#to solve this, another class like the fullname might be created but this could
#complicate things further and can break the code for everyone currently using the class.
#and they will have to go through and change the instance of the email attribute
#with an email method.

#property decorator can be used here just like getters and setters in java.


#this allows us to give our class attributes getters, ,setters and deleters functionalities.
class Student:
    #    class variable
    raise_allowance = 1.08
    num_of_students = 0

    # initialise(like constructor in java)
    def __init__(self, first, last):
        #        create instance variables
        self.first = first
        self.last = last

#        Here, I use Student rather than self because I constant value that can be
        # overwritten, as the number of Students applies to all. I use it under __init__
        # because it runs everytime I use the class on a new student object.

        Student.num_of_students += 1

#with this @property, we can access our email as attribute rather than as a function
#        which makes things better. An example is:
#        without the @property, you have to use the paranthesis after you call the email:
#        print(stud1.email())
#        but with the property, you can access it automatically right away:
#        print(stud1.email). See the latter part of the code for example of the usage.
        
    @property
    def email(self):
        return '{0}.{1}@helsinki.fi'.format(self.first, self.last).lower()

    # here, self has to be used as the parameter to make it function.
    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)
    
    
#stud1=Student('Oyedayo', 'Oyelowo')

print(stud1.first)
print(stud1.email)
print(stud1.fullname())


#now this should work also for the email without adding paranthesis.
#stud1.first = 'Blayz'
print(stud1.first)
print(stud1.email)
print(stud1.fullname())



#same can also be done to fullname. but when property is added to it, we might not be 
#able to get the parameters e.g
stud1=Student('Oyedayo', 'Oyelowo')
stud1.fullname = 'mand kiby'
print(stud1.first)
print(stud1.email)
print(stud1.fullname)

#when i added property to the fullname method, i got an error "AttributeError: can't set attribute" 
#while executing the above. so, it is better to keep it as it was if we need to set an attribue
#as above.

#To do set the fullname to something else, a setter can be used instead.(check above).
#the name of the property will be used as the setter.




#this allows us to give our class attributes getters, ,setters and deleters functionalities.
class Student:
    #    class variable
    raise_allowance = 1.08
    num_of_students = 0

    # initialise(like constructor in java)
    def __init__(self, first, last):
        #        create instance variables
        self.first = first
        self.last = last
        Student.num_of_students += 1
        
    @property
    def email(self):
        return '{0}.{1}@helsinki.fi'.format(self.first, self.last).lower()

    # here, self has to be used as the parameter to make it function.
    @property
    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last=name.split(' ')
        self.first=first
        self.last=last
        

#now, after adding the setter as above, it works properly without error unlike earlier
#whereby property added directly to the fullname method and new name reassigned to it
#e.gstud1.fullname = 'mand kiby'.

    
stud1=Student('Oyedayo', 'Oyelowo')
stud1.fullname = 'mand kiby'
print(stud1.first)
print(stud1.email)
print(stud1.fullname)


#deleter can be done in thesame way

class Student:
    #    class variable
    raise_allowance = 1.08
    num_of_students = 0

    # initialise(like constructor in java)
    def __init__(self, first, last):
        #        create instance variables
        self.first = first
        self.last = last
        Student.num_of_students += 1
        
    @property
    def email(self):
        return '{}.{}@helsinki.fi'.format(self.first, self.last).lower()

    # here, self has to be used as the parameter to make it function.
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last=name.split(' ')
        self.first=first
        self.last=last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first=None
        self.last=None
        
#e.g
stud1=Student('Oyedayo', 'Oyelowo')    
stud1.fullname = 'mafnd kibay'
print(stud1.first)
print(stud1.email)
print(stud1.fullname)

del stud1.fullname

       
