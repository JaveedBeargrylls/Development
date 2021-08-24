#program to execute the String with UserName given by user

import re

Username = input('Enter Your Name :')

if(re.findall('[A-za-z]{3,}',Username)): #ensuring the username contains min 3 characters
    print('Hello',Username,'How are you ?')
else:
    print("Enter the valid UserName")
