# Date - 19/11/2025
# day - 14 Bubble sort (Sorting algorithm)

def bubble_search(arr):
    n = len(arr)
    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

array = list(map(int, input("Enter a array element : ").split()))

print(bubble_search(array))
