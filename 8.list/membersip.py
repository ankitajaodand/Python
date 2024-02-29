#Membership operator 

a=[1,2,3,4,4,10]
x=a.count(4)# count of the element 4
print(x)
x=a.count(100)# count of the element 4
print(x)

if x>=0: 
    print("exists")
else: 
    ("doesnt exist")    

#method 2 
a=[1,2,3,4,4,10]   
num=4 

if num in a: 
    print("exists")
else: 
    print("doesnt exist")   