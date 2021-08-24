'''
@Author: Javeed
@Date: 2021-08-24
@Last Modified by: Javeed
@Last Modified time: 2021-02-11 21:30:00
@Title : Program Aim to get the output of 2 powerTable upto the given number
'''
def power_table(power):
    """
Description:
     Function to get the output of 2 powerTable upto the given number
Parameter:
      it takes power as a parameter that gives the power table upto the given numbers
Return:
       power table
"""
    for i in range(power+1):
        if(power <= 31):
            print('2','power',i,2**i)
        else:
            print("over flow")


#calling power_table function 
power_table(int(input('Enter the Nth number of power Table :')))