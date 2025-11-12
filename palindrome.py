# Date: 12/11/2025
# Day-07 - Palindrome number/string

#in this program revers the string formate only.
def palindrome(n):
    if n == n[::-1]:
        print(f"{n} is a palindrome.")
    else :
        print(f"{n} is not a palindrome.")


num = input("Enter a string: ")
print(palindrome(num))

def palindrome_number(n):
    original = n
    reverse = 0

    while n > 0 :
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    if original == reverse :
        print(f"{original} is a palindrome number.")
    else :
        print(f"{original} is not a palindrome number.")

number = int(input("Enter a number : "))
print(palindrome_number(number))