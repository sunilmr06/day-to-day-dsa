# Date : 11/11/2025 
# day - 6
# List of prime numbers

def is_prime(n):
    if n <= 0 :
        return False
    for i in range (2,int(n ** 0.5) +1):
        if n % i == 0 :
            return False 
    return True 

num = int(input("Enter a range of Prime number :"))

print("List of prime number is :", end= " ")

for i in range (2, num +1):
# here is_prime function check's every element is prime or not.
    if is_prime(i):
        print(i,end=" ")