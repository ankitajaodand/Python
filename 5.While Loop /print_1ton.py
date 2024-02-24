''''Print 0 to n'''

num:int=1

while num<=10: 
    print(num)
    num+=1

num:int=0
max=int(input("Enter maximum number of time= "))
while num<=max: 
    print(num)
    num+=1  



def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end=" ")
        i = i + 1
    print()

printPattern(10)
printPattern(5)
printPattern(47)    



