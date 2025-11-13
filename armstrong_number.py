# Date :13/11/2025
# day -8 Armstrong Number
# 153 → 1³ + 5³ + 3³ = 153 this is an armstrong number.
def armstrong_number(n):
    original = n
    num_digit = len(str(n))
    total = 0

    while n > 0 :
        digit = n % 10
        total += digit ** num_digit
        n //= 10

    if original == total :
        print(f"{original} is a armstrong number.")
    else:
        print(f"{original} is not a armstrong number.")

num = int(input("Enter a number : "))
print(armstrong_number(num))