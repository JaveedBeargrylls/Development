# Python program to get the Prime factors

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

def prime_factor(num):
    temp = num
    i = 2
    while temp > 1:
        if temp % i == 0:
            print(i,end=",")
            temp = int (temp/i)
        else:
            i = i + 1
prime_factor(int(input("Enter the Number")))