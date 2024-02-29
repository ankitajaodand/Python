'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

'''


for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()

#Method 2 

for i in range(1,6,1): 
    for j in range(4,i-1,-1): 
        print(' ',end=' ')
    for k in range(1,i*2,1): 
        print('*',end=' ')
    print()
for i in range(4,0,-1): 
    for j in range(i,5): 
        print(' ',end=' ')
    for k in range(i*2,1,-1): 
        print('*',end=' ')
    print()    
