'''
@Author: Javeed
@Date: 2021-08-24
@Last Modified by: Javeed
@Last Modified time: 2021-02-11 21:20:45
@Title : Program Aim to get the Harmonic series and harmonic number of user input
'''

def Harmonic_Number(number):
    """
Description:
     Function to get the Harmonic series and harmonic number of user input
Parameter:
      it takes number as a parameter that gives the harmonic number
Return:
       Harmonic series & Harmonic Number
"""
    harmonicNumber = 0
    for i in range(1,number+1):
        harmonicNumber = harmonicNumber + 1/i
        series = str(1)+"/"+str(i)
        print(series,end="")
        if(i == number):
            break
        else:
            print(end=" + ")
    print("\nHarmonic number of given number is :",harmonicNumber) 

#calling Harmonic_Number functions       
Harmonic_Number(int(input("Enter the Number :")))