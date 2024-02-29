#append 
'''Mutable objects are call by reference : call by reference means the changes in the variables will happen in the same memory location
if variable defined as local in the function and same variable is again defined as global then local also gets updated.
This is applicable only for mutable objects others are call by value they don't update the local variables in the memory '''
a=[1,2,3,4,5,6,7]
print(a)
print(id(a))
a.append(100)
print(a)
print(id(a))


#Insert 

a=[1,2,3,4,5,6,7]
a.insert(0,3)
print(a)


a=[1,2,3,4,5,6,7]
a.insert(3,110)#adds before the original index
print(a)



a=[1,2,3,4,5,6,7]
a.insert(100,110)#adds at the end since index out of range
print(a)

a=[1,2,3,4,5,6,7]
a.insert(-1,11000) #even in case of -ve index it adds before the original index value
print(a)




