num1 = num = int(input("Enter a number : "))
i = 0
while num >= 0:
    print(num,end=" ")
    num = num - 1

print("\n------------")

while i <= num1:
    print(i,end=" ")
    i = i+1

print("\n----------------")
num2 = int(input("Enter a number : "))
my_list = ["apple","653",'3.025','hello']
my_str = "Hello World"

print(num2)
print(my_list)
for x in reversed(range(num2)):
    if x != 0:
        print(x, end=" ")

print()
for word in my_list:
    for letters in word:
        print(letters,end="")
    print(",")
print()

for i in reversed(my_str):
    print(i, end=" ")
