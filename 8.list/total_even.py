'''Total number if even numbers in the list'''

a=[1,2,3,4,5,6,7,8,9,10]

total=0
for i in a: 
    if i%2==0: 
        total+=i
print(total)


# sum of numbers on the even index

total=0 
for i in range(0,len(a)): 
    if i%2==0:
        total+=a[i]
print(total)        


# Enumerate 


total=0 
for index,value in enumerate(a): 
    if index%2==0: 
        total+=i
print(total)