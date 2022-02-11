import math

v = float(input('Enter wind speed in miles per hour: '))
t = float(input('Enter the Temperature in Farenhite: '))

w = 35.74 + 0.6215*t + 0.4275*t*v**0.16 - 35.75*v**0.16      #formula for windchill

print('The WindChill is',float(round(w,0)))