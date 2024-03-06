'''If Else Using single line'''
 # when we use ternary before for loop then it is what to add
#when we use ternary before for loop then it is when to add

'''Print Adult if age age is greater than 18'''

age=20
print('Adult') if age>=18 else print('TeenAger') #ternary doesnt work without else


my_list=["Even" if i%2==0 else 'Odd' for i in range(0,10)] 
print(my_list)

my_list=[f"{i}-Even" if i%2==0 else f'{i}-Odd' for i in range(0,10)] # when we use ternary before for loop then it is what to add
print(my_list)

my_list=[i for i in range(0,10) if i%2==0] # when we use ternary after for loop then it is when to add
print(my_list)


