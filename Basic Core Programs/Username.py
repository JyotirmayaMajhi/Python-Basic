import re

Username = input('Enter your name: ')
temp = " Hello " +Username+ ", How are you??" .format(Username)

Match = re.match('[A-Z]{1}[a-z]{2,}$',Username)
if Match:
    print(temp)
else:
    print('Invalid')

