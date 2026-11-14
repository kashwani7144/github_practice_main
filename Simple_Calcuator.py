
import sys
# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Which Mathematical Operation do you want ?\n")
operator = input("Enter operator (+, -, *, /, %): ")

if operator == "+":
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is : {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Difference of {num1} and {num2} is : {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Product of {num1} and {num2} is : {result}")

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"Remainder of {num1} and {num2} is : {result}")
    else:
        print("Error! Modulus by zero is not allowed.")
        sys.exit(0)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Quotient of {num1} and {num2} is : {result}")
    else:
        print("Error! Division by zero is not allowed.")
        sys.exit(0)

else:
    print("Invalid operator!")
    sys.exit(0)
    
