a,b,c=(1,2,3)
print(a,b,c)


#Outputs are integer

a,b,c=0 #Not possible error since 0 is an integers and unpacking is possible with list and tuple only
print(a,b,c)


a,b,c=0,0,0 #This works since it makes it a tupple and unpacking works in tupple
print(a,b,c)

