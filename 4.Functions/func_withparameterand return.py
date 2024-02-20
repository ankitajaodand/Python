
'''By default function returs None if you don't return anything'''
def add(num1:int,num2:int,num3:int) -> int: 
    return num1+num2+num3

r=add(1,2,3)
print(r)


'''multiple return is done in tuple and we have to extract them as r,x=add(1,2,3)'''
def add(num1:int,num2:int,num3:int) -> tuple: 
    return num1+num2+num3,'checkoddeven'

r,x=add(1,2,3)
print(r,x)



'''' write 2 functions 
1. Add 3 integers
2. check the return of 1st function for oddeven 
'''
#we are creating two different function for these when not mandatory to increase the usability so that other developer can use only add or only evenodd
def add_1(num1:int,num2:int,num3)-> int: 
    return(num1+num2+num3)

def checkOddEven(num)-> None:
    if num%2==0: 
        print("even")
    else: 
        print("odd")

    
total=add_1(1,2,3)
checkOddEven(total)


''' create a function to check checkODDEven'''

"""
Make a function named checkOddEven
Which take 1 integer as a argument
If integer is Even, then Return True
If integer is Even, then Return True else return False
"""

def checkOddEven(num1:int)-> bool: 

    if num1%2==0: 
        return True
    return False

print(checkOddEven(2))
print(checkOddEven(11))

#Type 2
def checkOddEven(num1:int)-> bool: 
    return num1%2==0
    return False

print(checkOddEven(2))
print(checkOddEven(11))



