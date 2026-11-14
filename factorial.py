def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        factorial = num * fact(num-1)
        return factorial


num = int(input("Enter a number : "))

res = fact(num)

print(f"Factorial of {num} is : {res}")
