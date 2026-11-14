marks = [12,14,10,13,18,20,1,8,19,23]

upd_marks = []
for i in marks:
    upd_marks.append(i+2)

print("updated marks : ", upd_marks)

print("-----------------------------")

upd_marks1 = [i+2 for i in marks]

print("LC Updated Marks", upd_marks1)

print("-----------------------------")


def list_comp(num):
    global my_listc
    for x in range(num):
        element = input(f"Enter the list elements {x+1}: ")
        my_list.append(element)
        my_listc = [(int(i)+2) for i in my_list if int(i) >= 10]
    print(my_list)
    print(my_listc)


num = int(input("Enter the length of the list : "))
my_list = []

list_comp(num)



