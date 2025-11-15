# Date : 15/11/2025
# day - 10 basic_calculator.

def calculator(a,b,operation):
    

    if operation == "+" :
        sum = a + b
        print(f"sum of {a} and {b} is :{sum}")
    elif operation == "-" :
        sub = a - b
        print(f"subtraction of {a} and {b} is :{sub}")
    elif operation == "*" :
        mul = a * b
        print(f"multiplication of {a} and {b} is : {mul}")
    elif operation == "/" :
        if b == 0 :
            print("zero division error")
        div = a / b
        print(f"division of {a} and {b} is : {div}")
    else :
        print("Invalid operation.")

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a secoend number : "))
operatior = input("Enter a Operator (+, -, *, /) : ")
print(calculator(num1,num2,operatior))
  
