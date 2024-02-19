'''Q1. Write a program that takes two numbers as input and checks if the first
number is divisible by the second.'''

num1=int(input("Enter num1= "))
num2=int(input("Enter num2= "))

if num1%num2==0: 
    print(f"num1 {num1} is divisible by num2 {num2}")
else : 
    print(f"num1 {num1} is not divisible by num2 {num2}")

'''Q2. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.1. Print percentage of class attended2. Print Is student is allowed to sit in exam or not.
'''
classes_hld=int(input("enter total classes held= "))
classes_attended=int(input("enter classes attended= "))

per_attended=(classes_attended/classes_hld)*100
print(f"% of classes attended {per_attended:.2f}%") #:.2f adds the 2 decimal point and make it a float since : this is used it defining the data type 2 decimal type float

if per_attended > 75 : 
    print("Allowed for exam")
else :
    print("Not Allowed")

'''Q3. Write a program to check if number is divisible by 2 and 3 but not 8.'''
num=int(input("Enter the num= "))

if num%2==0 and num%3==0 and num%8!=0 : 
    print("number is divisible by 2 and 3 but not 8")
else: 
    print("number is not divisible by 2 and 3 but not 8")

'''Q4 Write a Python program that takes a student's score as input and prints the corresponding grade. Use the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
'''

mark= int(input("Enetr a number between 0-100= "))

if mark >= 90 and mark<=100 : 
    print("A")
elif mark >= 80 and mark<=89 : 
    print("B")
elif mark >= 70 and mark<=79 : 
    print("C")
elif mark >= 60 and mark<=69: 
    print("D")
elif mark >= 0 and mark<=60 : 
    print("Fail")
else: 
    print("Invalid Marks, It should be between 0-100")

'''Q5 Write a program to calculate bill. Ask the final amount from the user.You have to give discount
 and print the final bill after discount.
 50000 above - 30% discount
 40000 - 49999 - 25% discount
 30000 - 39999 - 20% discount
 10000 - 29999 - 10% discount
 1 - 9999 - No discountPrint the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000 You got 30% discountYour final bill is Rs. 56000'''

final_amt=float(input("Enter the final amount= "))

if final_amt >= 50000: 
    discount=30
elif final_amt>=40000 and final_amt<=49999: 
    discount=25
elif final_amt>=30000 and final_amt<=39999: 
    discount=20
elif final_amt>=10000 and final_amt<=29999: 
    discount=10
else: 
    discount=0    

billed_amount=final_amt-(final_amt*discount/100)
print(f"you got {discount:.2f}% as discount\n your final bill is {billed_amount}")

'''Q6. Ask 4 numbers from user. Make sure all the numbers entered by user are dierent. Print which number is the smallest.'''

# If you are using multiple AND conditions that is also OK

num1: int = int(input("Enter number 1: "))
num2: int = int(input("Enter number 2: "))
num3: int = int(input("Enter number 3: "))
num4: int = int(input("Enter number 4: "))

smallest = num1

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4

print(f"The smallest number = {smallest}")

'''Q7 Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment

'''
current_sal=float(input("Enter the final amount= "))

if current_sal< 10000: 
    increment=5
elif current_sal> 10000 and current_sal<=20000:
    increment=10
elif current_sal> 20000 and current_sal<=50000:
    increment=15
elif current_sal>= 50000 :
    increment=20 

updated_salry= current_sal+current_sal*(increment/100)  

print(f"The new salary is {updated_salry:.2f}")

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

year=int(input("enter the year= "))

if (year%4==0 and year%100!=0) or (year%4==0 and year%400==0): 
    print(f"{year} it's a leap year")
else: 
    print(f"{year} is not a leap year")





    


