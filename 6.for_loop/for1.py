
#Loop that accepts the range where first digit is inclusive and 2nd is not
#1 to 10

for i in range(1,11): 
    print(i)

#5 to 19

for i in range(5,20): 
    print(i)    

#in a user range 

start=int(input("Enter Start= "))
end=int(input("Enter End= "))   

for i in (start,end+1):
    print(i)



#Incrementer in for using step parameter , by default it is 1

for i in range(1,10,2):
    print(i)

#10 to 1

for i in range(10,0,-1) : 
    print(i)       
