# Date - 16/11/2025
#Day - 11 Find Maximum and Minimum in an Array

arr = list(map(int,input("Enter a array elements : ").split()))

maximum = arr[0]
minimum = arr[0]

for i in arr:
    if i > maximum :
        maximum = i
    if i < minimum :
        minimum = i

print("Maximum value : ",maximum)
print("Minimum value : ",minimum)
