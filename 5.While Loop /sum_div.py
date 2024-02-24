
def func(n1:int,n2:int)->int:
    i=1
    sum=0
    while i<=n1: 
        if i%n2==0: 
            sum+=i       
        i=i+1    
    return sum

print(func(64,3))