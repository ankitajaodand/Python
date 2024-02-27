def pattern1(n:int)-> None: 
    i=0
    sum=2
    while i<=n: 
        sum=sum+(i*20)
        print(sum+i*10*20,end=' ')
        i+=1
        


n=int(input("Enter the number= "))
pattern1(5)