def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        fct = 1
        for x in range(2, num+1):
            fct = fct * x
        return fct


num = int(input("Enter a number : "))

res = fact(num)
print(f"Factorial of {num} is : {res}")
