'''Q1. Make a list of your own. Print the whole list in reverse using FOR loop and WHILE loop.'''

a=[1,2,5,10,11,20]

for i in range(len(a)-1,-1,-1):
    print(a[i])


a=[1,2,5,10,11,20]
i=len(a)-1
while i>=0: 
    print(a[i])
    i-=1


