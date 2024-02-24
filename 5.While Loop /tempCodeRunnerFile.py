def pattern6(n:int)->int:
    i=1
    num=1
    while i<=n: 
        print(num)  
        if i%2:
            num=num+2
        else: 
            num=num+3
        i+=1

pattern6(10)            
          