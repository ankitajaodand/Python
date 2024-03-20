#Lambda Function 

'''
1. They are anonymus
2. Single line logic
3. lambda a,b:a+b :-> a and b are inputs and a+b is output
'''

add=lambda a,b: a+b
print(add(1,2))

'''create a lambda function that takes integer and it returns list containing 1 to n '''
make_list = lambda num: [i for i in range(1, num + 1)]
x = make_list(20)
print(x)

'''take input as list and return length''''

len_list=[[]]

add = lambda a, b: a + b
mul = lambda a, b, c: a * b * c if a != 0 and b != 0 and c != 0 else "Invalid"
make_list = lambda num: [i for i in range(1, num + 1)]
print(add(1, 5))
print(mul(4, 5, 0))
x = make_list(20)
print(x)

'''Sorted list'''

my_list = [["Anirudh", 76], ["Vandana", 23], ["Akul", 67], ["Sanjay", 92]]
# my_list = [[76, "Anirudh"], [23, "Vandana"], [67, "Akul"], [92, "Sanjay"]]
# print(my_list[0][0]) # 0th element of element 0 in list 1 
# print(my_list[2][1])
# print(my_list[3][-1])
# print(my_list[-4][0])
# my_list.sort() #This sorts by first element in the  each sublist  and doesn't return anything rather updates the same list , This is limited to list only since it's list method
# x = sorted(my_list) #This is function and can be applied to any data trype this doesnt update the same list rather it returns the list and sorts based on oll elements of list/sublist
# print(my_list)
# print(x)
my_list.sort(key=lambda x: x[1], reverse=True) #sort is used it internally traverses don't have to use loop,x is by default each element in the list it treversares automatically since
print(my_list) 

