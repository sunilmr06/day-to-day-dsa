# Date : 09/11/2025
# day - 4 Fibonacci (iterative)

#end=" " it's a parameter, helps to change what comes at the end 

def fibonacci(n):
    a,b = 0,1
    print("fibonacci serice: ", end=" ")
    for i in range (n):
        print(a,end=",")
        a,b= b,a+b

num = 7
print(fibonacci(num))

#Fibonacci (Recurction)

def fibonacci_recurtion(n):
    if n == 0 or n ==1 :
        return n
    else:
        return fibonacci_recurtion(n-1) + fibonacci_recurtion(n-2)
n =int(input("Enter a number :"))    
print("fibonacci Series:", end=" ")
for i in range (n):
    print(fibonacci_recurtion(i), end=",")
