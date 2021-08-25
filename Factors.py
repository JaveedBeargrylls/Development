'''
@Author: Javeed
@Date: 2021-08-24
@Last Modified by: Javeed
@Last Modified time: 2021-02-11 21:09:28
@Title : Program Aim to get the Prime factors
'''

def prime_factor(num):
    """
Description:
     Function to get the Prime factor numbers
Parameter:
      it takes num as a parameter that gives the prime factors upto the give number num
Return:
       prime factor numbers
"""
    temp = num
    i = 2
    while temp > 1:
        if temp % i == 0:
            print(i,end=",")
            temp = int (temp/i)
        else:
            i = i + 1

#calling the function
if __name__ == '__main__':
    prime_factor(int(input("Enter the Number")))


# def prime_factor(number):    
#     count = 0
#     for i in range(2,number+1):
#         if number%i == 0: #condition to get factor
#             for j in range(2,int(i/2)): #checking the above factor 
#                 if i%j == 0: # condition satisfied count to 1 and break
#                     count = 1
#                     break
#             if count == 0: # if count 0 print i its prime factor number
#                 print(i)
# prime_factor(45)
