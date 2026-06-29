# Date : 17/11/2025.
# day -12 Linear search variants.

def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target :
            print(f"Element found at : {i}")
    # here we can use break statement for item there in multiple times but we need first found        
    else: 
        print ("element not found")


array = list(map(int,input("Enter the elements of the array :").split()))

target = int(input("Enter the target number : "))

print(linear_search(array,target))
