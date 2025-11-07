#Date : 07/11/2025
# day 2: Sum of n numbers.

def sum_of_n_numbers(n):
    total =0
    for i in range (1,n+1):
        total += i
    return total

#exeemple 
num = int(input("Please enter a positive valune :"))
print (f"The sum of first {num} numbers is : {sum_of_n_numbers(num)}")
