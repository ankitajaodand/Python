#1+2+3 till n 

start:int= int(input("Enter M= "))
end:int= int(input("Enter N= "))

i:int=start
total:int=0
while i<=end: 
    total=total+i
    i+=1
    
print(f"Addition of numbers from {start} to {end} is {total}")    