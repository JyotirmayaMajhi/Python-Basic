import cmath  #module for complex math

a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

d = (b*b) - (4*a*c) #calculate delta

Root_1_of_x = (-b + cmath.sqrt(d))/(2*a)
Root_2_of_x = (-b - cmath.sqrt(d))/(2*a)

print(Root_1_of_x)
print(Root_2_of_x)