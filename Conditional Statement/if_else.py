'''
conditional statements
IF 
ELSE 
ELIF

'''

#IF ElseIF
age= int(input("Enter age= "))

if age>18: 
    print("You are eligible") # condition satisfies executes below 3
    print("Congratulations")
    print("Please proceed")
else: # If condition doesnt satisfy, this is optional not cumpulsory
    print("Not eligible") 
print("Bye")    # In both the cases since its out of If statement

# Even ODD no 

num=int(input("Enter a number="))

if num%2==0: 
    print(f"{num} is even")
else : 
    print(f"{num} is odd")






