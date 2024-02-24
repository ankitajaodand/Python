#1,2,4,8,15,64.........

def pattern_mul2(n:int):
    i=1
    number=1
    while i<=n: 
        number=number*2
        print(number)
        i+=1


pattern_mul2(10)
