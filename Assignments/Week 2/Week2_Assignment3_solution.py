'''
Q1. Create a function named div_by_3_and_5 which takes 2 integers as a arguments (n1,n2), 
and print all the numbers divisible by 3 and 5 between n1 and n2
'''

def div_by_3_and_5(n1:int,n2:int)->int: 
    i=n1
    while i<=n2: 
        if i%3==0 and i%5==0: 
            print(f"{i}")
        i+=1

div_by_3_and_5(1,50)   


'''Q2. Create a function named calSum() which takes 2 integers n1 and n2 as a argument. 
Calculate the sum of all the numbers from n1 and n2 and 
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not, then return “n1 should be smaller”.
'''

def calSum1(n1:int,n2:int)->int: 
    i=n1
    sum=0
    if i<=n2:  
        while i<=n2: 
            sum+=i
            i+=1
    else: 
        print("n1 should be smaller")
    return sum 

print(calSum1(1,10))
print(calSum1(10,1))


'''Q3. Create a function named multiplicationTable that takes an integer 
num as an argument. Print the multiplication table of that number up to 10 numbers.'''

def multiplicationTable(num1:int)->int: 
    i=1
    while i<=10: 
        print(f"{num1} * {i}={num1*i}")
        i+=1

multiplicationTable(5) 


'''Q4. Create a function named calSum which takes an 2 integer (n1 and n2) 
as an argument. 
Calculate the sum of all the numbers divisible by 5 between n1 and n2 and return that sum. (Make sure that n1 is less than n2).'''

def calSum(num1:int,num2:int)->int: 
    sum=0
    i=num1
    if num1<=num2:
        while i<=num2: 
            if i%5==0:
                sum+=i
            else:
                sum+=0
            i+=1     
               
    else: 
        print(" n1 should less than n2")

    return sum

sum=calSum(43,68)
print(sum)

'''Q5. Create a function named printPattern that takes one integer (num) as an argument. Print from -num to num. 
Also keep in mind number passed as an argument can be negative or positive.'''

"""
Ask a number from user = 50
-50 to 50
Ask a number from user = 10
-10 to 10
Ask a number from user = -13
13 to -13
Ask a number from user = -20
20 to -20
"""

def printPattern(number:int)->int:
    if number > 0:
        start = -number
        end = number
        while start <= end:
            print(start, end=" ")
            start += 1
    else:
        start = -number  # 20
        end = number  # -20
        while start >= end:
            print(start, end=" ")
            start -= 1   


number: int = int(input("Enter a number = "))  # -20  
printPattern(number)      




    








