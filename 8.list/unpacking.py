a,b,c=[1,2,3]
print(a,b,c)

#Outputs are integer

a,b,c=0 #Not possible error 
print(a,b,c)


a,b,c=0,0,0 #This works
print(a,b,c)


a,b,*c =1,2,3,4,5,6

print(a)
print(b)
print(c)


a,*b,c =1,2,3,4,5,6

print(a)
print(b)
print(c)


