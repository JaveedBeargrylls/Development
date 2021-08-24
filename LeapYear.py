# Python program to check if year is a leap year or not

def Check_LeapYear(Year):  
    # Checking if the given year is leap year or not
    # if year is divisible by 4 & 400 then is_leap_year 
    # if year is divisible by 100 then not_leap_year
  if((Year>999) and (Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
      print("Given Year is a leap Year");  
  else:
      print ("Given Year is not a leap Year")  
  
Year = int(input("Enter the year: "))  
# Printing result  
Check_LeapYear(Year)