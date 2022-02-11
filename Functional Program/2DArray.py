row = int(input("Number of rows:"))
col = int(input("Number of columns:"))

matrix = []
print("Enter the entries row wise:")

for i in range(row):     #i for row
    a = []
    for j in range(col):  #j for column
        a.append(int(input()))
    matrix.append(a)          # elements of "a" pushed to matrix
print("The 2D array is:")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()