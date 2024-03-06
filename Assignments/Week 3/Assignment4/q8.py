'''Q8. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.'''

input_lst=[]
for i in range(0,10): 
    num=int(input("enter the number= "))
    input_lst.append(num)
print(input_lst)

reverse_lst=[]

for i in range(len(input_lst) - 1, -1, -1):
    reverse_lst.append(input_lst[i])

print(reverse_lst)

