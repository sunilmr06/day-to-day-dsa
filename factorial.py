# Date : 08/11/2025
# program number 3 
# Factorial of a number using iterative and recursive method 

#factorial using itretive method
def factorial (n):
    fact = 1
    if n < 0:
        print("Enter a positive value")
    else:
        for i in range (1,n+1):
            fact *= i
        print(fact)



#factorial using recursion 
# Recursion = function call itself, breaking the problem into smaller  
def fact_recursion(n) :
    if n == 0 or n == 1:
        return 1
    else :
        return n * fact_recursion(n-1)
    
num = int(input("Enter a number :"))
print(factorial(num)) 
print(fact_recursion(num))