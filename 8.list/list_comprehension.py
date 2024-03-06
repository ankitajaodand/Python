'''List comprehension is used to create the list'''


#Regular Method
my_list=[]

for i in range(1,10): 
    my_list.append(i)
print(my_list)

#List Comprehension

my_list=[i for i in range(0,10)] #here i the one that gets appended 
print(my_list)

my_list=[1 for i in range(0,10)] #here 1 gets appended till the valid range of 0-10 that is 10 times
print(my_list)

my_list=[i+5 for i in range(0,10)] #here i+5 the one that gets appended 
print(my_list)

my_list=[i%2 for i in range(0,101,5)] #here i%2 the one that gets appended 
print(my_list)


my_list=[i for i in range(0,101,5)] #here i the one that gets appended 
print(my_list)

my_list=[i for i in range(-1,-10,-1)] #here i the one that gets appended 
print(my_list)

my_list=[i for i in range(-10,-1,-1)] #here i the one that gets appended 
print(my_list)

my_list=[i%2==0 for i in range(0,10)] #here i which is true or false the one that gets appended 
print(my_list)





