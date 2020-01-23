""" This is the main function.
    prerequisite:
    based on Python 3.6
    
    Function
    ---------
    find the minimum in a random array which has 'n' members and sort 
    
    Parameters
    ---------
    number: int
        the length of random array
"""

######################################

import argparse
import numpy as np
from datetime import datetime

######################################

def readCommands():
    # function description for use within python
    """
    Read commandline arguments
    """
    # create an argparse object with a useful help comment
    p = argparse.ArgumentParser(description=("An illustration of a command line parser"))
    # read an integer
    p.add_argument("--numb", dest="numb", type=int, default=40, help=("Length of array to generate\nDefault=40"))
    # parse the command line into an object
    cmdargs = p.parse_args()
    # return that object from this function
    return cmdargs
    
    
class dataSorter(object):
    # an attribute
    numb_accounts=0
    
    # creation method
    def __init__(self,number=10): # the default length of array is 10
        print("Creating a class") 
        self.number=number # set the length of array 
        dataSorter.numb_accounts+=1 # add an instance to 'dataSorter' class
       
    # methods
    def findMini(self):
        """
        generate an array of random  numbers; use outer loop to loop over the array 
        and inner loop to compare every 2 numbers once
        """
        n = self.number 
        t0 = datetime.now() # return system time
        arr=np.random.random(n) # generate an array of random numbers
    
        print("The original array is") # print the random array before sorting 
        print(arr) 

        for i in range(n): # loop over the random array from the first number
            for j in range(i): # compare the origin number with every number before it
                if (arr[i]<arr[j]): # if the target number is smaller than origin number,
                                    # swap them
                    s= arr[j] 
                    arr[j] = arr[i]
                    arr[i] = s
            
    
        t1 = datetime.now()  # return system time
        duration = t1 - t0 # calculate the time of looping to find the minimum

        print("The minimum number is ",arr[0]) # print the minimum of the random array
        print("The processing last ",duration) # print the  processing time of finding minimum
        print("The list in ascending order is ")# print out the random array in ascending order
        print(arr)

############################r)
                        
if __name__ == '__main__':
    """
    Main block
    """
    cmd = readCommands() # read the command line
    y = dataSorter(); # generate an instance of class
    y.findMini() # call function 'findMini()' to sort the array
    