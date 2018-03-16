'''
Created on Jun 7, 2016

@author: 174500
'''
import random

def randDice():
    print ("*****************************\n\nThis is a dice simulation. It will output a random " + 
    "integer between 1 and 6.\n\n")
    num = random.randrange(1,6)
    print("The die rolled a ", num) 
    cont = input("\n\nWould you like to continue? ") #in python3, raw_input( is now input()
    if "yes" in cont:
        randDice()
    else:
        exit()
randDice()