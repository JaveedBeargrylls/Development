'''
@Author: Javeed
@Date: 2021-08-24
@Last Modified by: Javeed
@Last Modified time: 2021-02-11 21:42:15
@Title : Program Aim to get the percentage of heads and tails of a flipped coin
'''
import random

def flip_coin(count): #creating the function flip_coin    
    """
Description:
     Function to get the percentage of heads and tails of a flipped coin
Parameter:
      it takes count as a parameter that gets the percentage of heads and tails of a flipped coin using random function
Return:
       percentage of heads and tails of a flipped coin and count of the heads and tails
"""
    heads = 0
    tails = 0
    headspercent = 0 
    tailspercent = 0 

    for i in range(count):#step
        coin=random.randint(1,2) # assign a value to coin, either 1 or 2
        if coin==1: # if coin value is assigned as 1
            heads+=1 # increase heads count by 1
        else: # if coin value is assigned something other than 1
            tails+=1 # increase tails count by 1

        headspercent = (heads / count) * 100 
        tailspercent = (tails / count) * 100 
    print("Heads",heads)
    print("Tails",tails)
    print("Heads percent: ",'%.2f'%headspercent) # using "%" to print value till 2 decimal places
    print("Tails percent: ",'%.2f'%tailspercent) 

#calling flip_coin function
flip_coin(int(input('Enter Number of time to flip the coin :')))

