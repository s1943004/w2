""" This is the main function.
    prerequisite:
    based on Python 3.6
    
    Function
    ---------
    save bank account information of users (incl. name, balance, number of accounts);
    create account, add deposite, withdraw money, inquiry balance, deduct tax.
    
    Parameters
    ---------
    name: string
        the name of account owner
    balance: int
        the balance of account owner
"""

######################################

import numpy as np

######################################

class yourBank(object):
    
  # an attribute
  numb_accounts=0
  
  # creation method -- create account
  def __init__(self,name,balance):
    print("Creating a class")
    self.name=name
    self.balance=balance
    yourBank.numb_accounts+=1 # count the number of account owner
    
  # methods
  def deposit(self,amt):
    self.balance=self.balance+amt # add deposite 
  def withdraw(self,amt):
    self.balance=self.balance-amt # withdraw money
  def inquiry(self):
    return self.balance # inquiry balance
  def tax(self,rate):
    self.balance=self.balance-self.balance*rate # deduct tax

# new classes 'myBank', inheriting from old class 'yourBank' 
class myBank(yourBank):
    
  # overloading pre-defined method 'inquiry()'
  def inquiry(self):
    a = np.random.random(1) # set the value of 'a' randomly from 0 to 1
    if a< 0.3: # when the random variable 'a' is less than 0.3, system will lie
      return self.balance*1.1; # increase how much you have by 10% to lie
    else:
      return self.balance;

