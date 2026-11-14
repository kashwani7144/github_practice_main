def mul_tables(num, rng, init):
    for i in range(init,rng):
        print(f"{num} x {i} = {num*i}")


num = int(input("Enter a number : "))
init = int(input("Enter initial range : "))
rng = int(input("Enter a max range : "))
mul_tables(num, rng, init)
