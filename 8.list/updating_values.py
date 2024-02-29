'''Updating values in the list'''

a=[1,2,3,100,200,400]

#print(a[1])

#a[1]=100

#print(a[1])

'''Add 1 in even numbers and -1 for odd numbers in the list'''

for index,values in enumerate(a): 
    if values%2==0: 
        a[index]=a[index]+1
    else: 
        a[index]=a[index]-1
print(a)

'''position odd then +1 and even then -1'''

a=[1,2,3,100,200,400]
for index,value in enumerate(a): 
    if index%2==0: 
        a[index]=a[index]+1
    else: 
        a[index]=a[index]-1

print(a)


#Method 2 

