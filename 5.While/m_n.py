'''Print M to N asking user'''

m:int= int(input("Enter M= "))
n:int= int(input("Enter N= "))

i:int=m
while i<=n: # using i and not m because it will change the dataset
    print(i,end='')
    i+=1 
print()

'''Ask M and N from user 
IF M < N THEN M TO N 
IF N<M THEN N TO M'''

m:int= int(input("Enter M= "))
n:int= int(input("Enter N= "))

if m<=n: 
    i:int=m 
    max:int=n
else: 
    i:int=n
    max:int=m
while i<=max: 
    print(i)
    i+=1


m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))
i:int=m
j:int=n
if m<=n:
	while i<=n:
		print(i,end=" ")
		i+=1
else: 
	while j<=m:
		print(j,end=" ")
		j+=1
print()    

#Method 2
m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))
i:int=m
j:int=n
if m<=n:
	while i<=n:
		print(i,end=" ")
		i+=1
else: 
	while j<=m:
		print(j,end=" ")
		j+=1
print()
