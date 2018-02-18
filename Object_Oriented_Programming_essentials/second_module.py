# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:47:20 2018

@author: oyeda
"""

#import first_module
#print("second module's name: {}".format(__name__))

#by using just this:"print("First module's name: {}".format(__name__))", in the
#first module(script),
#The above produced the below because, the first is being imported while the second
#is being run by python
#First module's name: first_module
#second module's name: __main__


import first_module
#thisnow produces run from(which was defined in the first module) import because 
#it is being imported

print("second module's name: {}".format(__name__))
#this produces main, because it is being run directly

#this can be imported this way, if all the statements are put under the main
#function in the first_module/script
first_module.main()

