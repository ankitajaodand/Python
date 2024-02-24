
def factor(n1:int)-> None: 
    i=1
    while i<=n1:
        if n1%i==0:
            print(i)
        i+=1    

factor(12)

# check if the count of factor is prime or not , the number divisible by only one and itself then prime


def factor(n1:int)-> int: 
    i=1
    count:int=0
    while i<=n1:
        if n1%i==0:
            print(i)
            count+=1

        i+=1    
    return count

#method 1

if factor(5)==2: 
    print("Number is Prime")
else : 
    print("Number is not prime")


 def isprime(n:int)-> bool: 
    count=factor(n)   
