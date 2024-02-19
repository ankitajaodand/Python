'''Q1. Write a Python function to find the Maximum and minimum of three numbers. Use 3 parameters. Make 2 different functions named as maxi and 
mini'''

def findMinimum(num1:int,num2:int,num3:int):
    small=num1
    if small>num2: 
        small=num2
    if small > num3:
        small=num3
    return small 
    
output=findMinimum(9,7,4) 
print(output)   



def findMaximum(num1:int,num2:int,num3:int):
    max=num1
    if max<num2: 
        max=num2
    if max<num3:
        max=num3
    return max 
    
output=findMaximum(10,11,13) 
print(output)   


'''Q2. Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but using function. 
Try calling function with dierent years as a parameter and check the output.'''

'''Q8. An extra day is added to the calendar almost every four years as
February 29, and the day is called a leap day. A leap year contains a leap
day.
These are the conditions used to identify leap years:
if the year can be evenly divided by 4, it is then a leap year
but if the year is evenly divided by 4 and also by 100, then it is NOT a
leap year
but if the year is evenly divided by 4 and also by 400, then it is a leap
year
This means the years 2000 and 2400 are leap years, while 1800, 1900,
2100, 2200, 2300 and 2500 are NOT leap years.
Ask a year input from user. And tell if the year entered by user is leap or
not.'''

def leapYear(year:int):
    
    if year%4==0 and year%100!=0:
        print(f"{year} is a leap year")
    elif year%4==0 and year%400==0: 
        print(f"{year} is a leap year")
    else : 
        print(f"{year} is not a leap year") 

year=int(input("Enter Year= ")) 
leapYear(year)        

#solution 2 
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")    

'''Q3.  Attempt the same bill calculator question (Week 1 - Assignment 2 - Q5) 
but using function. Try calling function with dierent bill amount as a parameter and check the output.'''


'''Q4 Write a Python program that takes a student's score as input and prints the corresponding grade. Use the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
'''

def printGrade(score:int):
    if score>=90 and score>=100: 
        print("A")
    elif score>=80 and score<90: 
        print("B")
    elif score >=70 and score < 80:
        print("C")
    elif score>= 60 and score<70: 
        print("D")
    else: 
        print("Below 60")  

input_score=int(input("enter score:"))
printGrade(input_score)          

'''Q4. Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7) using function.'''
'''Q6. Ask 4 numbers from user. Make sure all the numbers entered by user are dierent. Print which number is the smallest.'''

num1: int = int(input("Enter number 1: "))
num2: int = int(input("Enter number 2: "))
num3: int = int(input("Enter number 3: "))
num4: int = int(input("Enter number 4: "))

def printSmallest(num1:int,num2:int,num3:int,num4:int): 
    smallest=num1
    if num1>num2: 
        smallest=num2
    if smallest>num3: 
        smallest=num3
    if smallest>num4: 
        smallest=num4
    print(f"Smallest {smallest}")  

printSmallest(num1,num2,num3,num4)      

'''Q7 Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment

'''

salary=float(input("Enter Salary "))
def salaryIncrement(salary:float): 
    if salary <= 10000: 
        incr=5
    elif salary > 10000 and salary >= 20000: 
        incr=10
    elif salary > 20000 and salary >= 50000: 
        incr=15
    else: 
        incr=20    
    updated_salary=salary+salary*(incr/100)  
    print(f"updated_salary: {updated_salary}")

salaryIncrement(salary)      
    

