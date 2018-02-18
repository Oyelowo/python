# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:29:25 2018

@author: oyeda
"""



#when python runs a file, it first sets some special variables and name is one
#of them.
#when python runs a python file directly, it sets the name=__main__
#print("First module's name: {}".format(__name__))


##this can help tp check if the file is being run directly by python or it is 
##being imported.

def main():
#    print("first module's name: {}".format(__name__))
    if __name__ == '__main__':
        print("run directly")
    else:
        print("run from import")

#thisis important because sometimes,, you want to know if you're running a 
#a file directly or ir it is being imported
        
main()
