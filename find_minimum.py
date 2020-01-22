""" This is the main function.
    prerequisite:
    based on Python 3.6
    
    Function
    ---------
    find the minimum in a random array which has 'n' members 
    
    Parameters
    ---------
    n: int
        the number of rows or columns of the chessboard
"""

######################################
import numpy as np
from datetime import datetime

######################################
class Minimum(object):
    # an attribute
    numb_accounts=0
    
    # creation method
    def __init__(self,number):
        print("Creating a class")
        self.number=number
        Minimum.numb_accounts+=1
       
    # methods
    def findMini(self):
        """
        generate an array of random  numbers; use outer loop to loop over the array 
        and inner loop to compare every 2 numbers once
        """
        n = self.number # 
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
                        

    