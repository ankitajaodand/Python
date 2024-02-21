
n:int=1
m:int=100
i:int=n
count:int=0
while i<=m: 
    if i%2==0: 
        count+=1
    i+=1    
   
print(f"count: {count}")