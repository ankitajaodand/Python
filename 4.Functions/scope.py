'''
local variables : where the scope is only limited to the funstions since it's defined inside functions
'''

def add():
    #local variables
    num1=int(input("enter num1 = "))
    num2=int(input("enter num2 = "))
    print(num1+num2)

add()
# Global variables since they are outside the functions
num1=1
num2=200
print(num1,num2) #this prints global variables and not the local variables 


# function always returns some output if we don't define return then it retruns None

x=add()# x will have None since nothing is written from add()
