
# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is : {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Difference of {num1} and {num2} is : {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Product of {num1} and {num2} is : {result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Quotient of {num1} and {num2} is : {result}")
    else:
        result = "Error! Division by zero is not allowed."

else:
    result = "Invalid operator!"
    
