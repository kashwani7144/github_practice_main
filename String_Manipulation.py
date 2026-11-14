import re

#inpput a string from user

inp_str = input("Enter an input String : ")
print("---------------------------------------------------------\n")
#1. reverse it and check for palindrome

rev_str = inp_str[::-1]
print(f"Reverse of {inp_str} is {rev_str}")
if (inp_str == rev_str):
    print(f"{inp_str} is Palindrome.\n")
else:
    print(f"{inp_str} is NOT a palindrome.\n")
print("---------------------------------------------------------\n")

#2. count each charachers of the inp_str

freq = {}
for i in inp_str:
    freq[i] = inp_str.count(i)
print("Frequency of each word is : ")
print(freq)
print("---------------------------------------------------------\n")

#3. Seprate alphabets, numbers and special characters from the inp_str

alpha = re.sub(r'[^a-zA-Z]','',inp_str)
print(f"Alphabets are : {alpha}\n")

num = re.sub(r'[^0-9]','',inp_str)
print(f"Numbers are : {num}\n")

spec_char = re.sub(r'[a-zA-Z0-9]','',inp_str)
print(f"Special Characters are : {spec_char}\n")

