# Python program to get the Harmonic series and harmonic number of user input


def Harmonic_Number(number):
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
Harmonic_Number(int(input("Enter the Number :")))