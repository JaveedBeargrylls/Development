# Python program to get the output of 2 powerTable upto the given number

def power_table(power):
    for i in range(power+1):
        if(power <= 31):
            print('2','power',i,2**i)
        else:
            print("over flow")
    
power_table(int(input('Enter the Nth number of power Table :')))