my_list = ["apple","orange","banana","236",963,True,0.256,"ashwani256","orange","apple",False]
my_list1 = list(("apple","orange","banana","ashwani256","orange","apple"))
print(f"List is {my_list}")
print(f"List1 is {my_list1}")
if 963 in my_list:
    print("yes")
else:
    print("no")
list2 = my_list + my_list1
my_list.insert(2,"cabbage")
print(my_list)
my_list.extend(my_list1)
print(my_list)
print(f"list 2 : {list2}")
