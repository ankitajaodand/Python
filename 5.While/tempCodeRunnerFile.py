num:int=int(input("Enter number"))

if num>=0: 
    i=num-(num*2)
    while i<=num:
        print(i)
        i+=1
else: 
    i=num+(num*-2) 
    print("i is",i)
    while i>=num:#num=-10 and i=10
        print(i)
        i-=1