'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

'''

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(2 * i - 1, 0, -1):
        print("*", end=" ")
    print()


# method 2 

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    for l in range(1, i):
        print("*", end=" ")
    print()        