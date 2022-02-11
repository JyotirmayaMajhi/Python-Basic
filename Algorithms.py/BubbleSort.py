def bubblesort(Num):
  
  for n in range(len(Num)-1, 0, -1):        # Looping from size of array from last index[-1] to index [0]
    for i in range(n):
      if Num[i] > Num[i + 1]:
        
        Num[i], Num[i + 1] = Num[i + 1], Num[i]  # swapping data if the element is less than next element in the array

Num = [10,8,6,4,2,1,0]
  
print("Unsorted list is,") 
print(Num)
bubblesort(Num)
print("Sorted Array is, ")
print(Num)