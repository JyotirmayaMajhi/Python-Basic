Year = 2004

if( Year % 400 == 0) and ( Year % 100 == 0) or ( Year % 4 == 0) :
    print("Year is a Leap Year" .format(Year))
# elif( Year % 4 == 0) and ( Year % 100 != 0):
#     print("Year is a Leap Year" .format(Year))
else:
    print("Year is not a Leap Year")
