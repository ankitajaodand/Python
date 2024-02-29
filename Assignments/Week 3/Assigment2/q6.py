'''
7 
6 7 
5 6 7 
4 5 6 7 
3 4 5 6 7 
2 3 4 5 6 7 
1 2 3 4 5 6 7 
2 3 4 5 6 7 
3 4 5 6 7 
4 5 6 7 
5 6 7 
6 7 
7 

'''





def pattern(n: int) -> None:
    for i in range(n // 2 + 1, 0, -1):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()
    for i in range(2, n // 2 + 2):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()



for i in range(7,0,-1): 
    for j in range(i,i-1,-1):
        print(j,end=' ')
    print( )    