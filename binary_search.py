# Date : 18/11/2025
# day - 13 Binary search

def binary_search(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high :
        mid = (low + high) // 2

        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = list(map(int,input("Enter the array element : ").split()))
target = int(input("Enter the target value : "))


print(binary_search(array,target))

