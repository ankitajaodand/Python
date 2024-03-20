'''
Map needs one function and iterable 
map retutns map object we need to convert it to list or set
functions can be predefined or user defined
'''

'''Adding one to every number'''
a=[1,2,3,4,5,6]

def change(n):
    return n+1

print(list(map(change,a)))  #we are writting list just to review the output since map create the object 


'''Taking the numbers in the single line from user'''

a=input("enter numbers'")

x,y,z,a=list(map(int,a.split()))
print(x,y,z,a)

#single line
a,b,c,d=list(map(int,input("enter 4 numbers ").split()))
print(a,b,c,d)


