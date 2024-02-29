'''Triversing the elements using look'''

a=[1,2,3,4,10,11,12,15]



i=0
while i< len(a): 
    print(a[i])
    i+=1

for i in range(0,8): 
    print(a[i])


for i in range(0,len(a)): 
    print(a[i])

for i in range(-8,-1,-1):
    print(a[i]) 

a=[1,2,3,4,10,11,12,15]
for i in range(len(a)-1,-1,-1):
    print(a[i])
    





