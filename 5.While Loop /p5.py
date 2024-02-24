#1, 11,101,1001,1001


def pattern5(n:int): 
    i=1
    number=1
    mul=1
    while i<n:
        print(number*mul+number)
        mul=mul*10
        i+=1

pattern5(10)


#Method 2 
def pattern5_2(n:int): 
    i=1
    