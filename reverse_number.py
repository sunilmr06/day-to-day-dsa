# Date : 14/11/2025
# day - 9 Reverse A Number 

def reverse_number(n):
    original = n
    reverse = 0

    while n > 0 :
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    print(f"Reverse of {original} is {reverse}")

num = int(input("Enter a number : "))
print(reverse_number(num))

# This Reverse string format.
def reverse_string(n) :
    reverse = n[::-1]

    print(f"Reverse of {n} is {reverse}")

value = input("Enter a string : ")
print(reverse_string(value))

