'''
@Author: Javeed
@Date: 2021-08-24
@Last Modified by: Javeed
@Last Modified time: 2021-02-11 21:42:08
@Title : Program Aim to check if year is a leap year or not
'''

def check_leapYear(Year):  
    """
Description:
     Function to check if year is a leap year or not
Parameter:
      it takes year as a parameter that checks the year is leap year or not
Return:
       leap_year or not
"""
    # Checking if the given year is leap year or not
    # if year is divisible by 4 & 400 then is_leap_year 
    # if year is divisible by 100 then not_leap_year
    if((Year>999) and (Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
          print("Given Year is a leap Year");  
    else:
          print ("Given Year is not a leap Year")  

if __name__ == '__main__':
    check_leapYear(int(input("Enter the year: "))) 