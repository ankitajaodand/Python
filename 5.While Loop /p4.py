# 1 11 101 1001 10001 100001


def pattern4(n:int): 
    i=1
    number=1
    mul=1
    while i<n:
        print(number*mul+number)
        mul=mul*10
        i+=1

pattern4(10)

