'''
        *
      * * 
    * * *
  * * * *
* * * * *

'''

for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(i,):
        print('*',end=" ")
    print()

#Method 2
    
for i in range(1,6): 
    for j in range(4,i-1,-1): 
        print(' ',end=' ')
    for k in range(1,i+1): 
        print('*',end=' ')
    print()

