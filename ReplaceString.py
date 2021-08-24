'''
@Author: Javeed
@Date: 2021-08-24
@Last Modified by: Javeed
@Last Modified time: 2021-02-11 21:50:37
@Title : Program Aim to execute the String with UserName given by user
'''
import re

Username = input('Enter Your Name :')

if(re.findall('[A-za-z]{3,}',Username)): #ensuring the username contains min 3 characters
    print('Hello',Username,'How are you ?')
else:
    print("Enter the valid UserName")
