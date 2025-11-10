# Date : 10/11/2025
# Day - 5  Prime check (sqrt method)

def is_prime(n):
    if n <= 0:
        return False 
# here we check the number 2 to squre root of the number.
    for i in range (2,int(n ** 0.5) + 1):
        if n % i == 0 :
            return False 
    return True

num = int(input("Enter a number : "))
if is_prime(num) :
    print(f"{num} is a prime number.")
else :
    print(f"{num} is not a prime number.")