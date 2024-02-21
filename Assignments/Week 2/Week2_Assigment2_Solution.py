'''Q1. Create a function that takes three numbers as parameters and returns the largest among them. 
Also if no arguments are passed, make sure the parameters take default value as None and return answer as -1'''

def largestNumber(num1:int,num2:int,num3:int)-> int: 
    if num1!=None and num2!=None and num3!=None: 
        if num1>=num2 and num1>=num3: 
            return num1 
        elif num2>=num1 and num2>=num3: 
            return num3 
        else: 
            return num3
    else: 
        return -1

largest_no=largestNumber(4,4,7)
print(largest_no)
largest_no=largestNumber(4,7,7)
print(largest_no)
largest_no=largestNumber(4,5,8)
print(largest_no)
largest_no=largestNumber(8,2,1)
print(largest_no)
largest_no=largestNumber(8,2,9)
print(largest_no)
largest_no=largestNumber(8,8,1)
print(largest_no)

#Method 2
def largest_part2(num1: int, num2: int, num3: int) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1 

largest_no=largest_part2(4,4,7)
print(largest_no)
largest_no=largest_part2(4,7,7)
print(largest_no)
largest_no=largest_part2(4,5,8)
print(largest_no)
largest_no=largest_part2(8,2,1)
print(largest_no)
largest_no=largest_part2(8,2,9)
print(largest_no) 
largest_no=largest_part2(8,8,1)
print(largest_no)            
    


##Method 2
def largest_part2(
    num1: int | None = None, num2: int | None = None, num3: int | None = None
) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1    
    
'''Q2. Implement a function that takes two parameters, base and exponent, and returns the result of raising the base to the power of the exponent.'''

def raisetoPower(base:int,exponent:int)->float: 
    return(base**exponent)

base_value = 2
exponent_value = 3
result_power = raisetoPower(base_value, exponent_value)
print(f"{base_value} raised to the power of {exponent_value} is: {result_power}")

'''Q3. Ask 3 numbers from user. Make a function which returns the middle of those 3 numbers. 
Then make a function to check if that middle number is divisible by both 3 and 4. Make 2 functions for reusability'''

def middleNumber(num1:int,num2:int,num3:int)->int: 
    if num1>=num2 and num1<=num3 or num1<=num2 and num1>=num3: 
        return num1
    if num2>=num3 and num2<=num1 or num2<=num3 and num2>=num1: 
        return num2
    else: 
        return num3
    
middle_no=middleNumber(4,4,7)
print(middle_no)
middle_no=middleNumber(4,7,7)
print(middle_no)
middle_no=middleNumber(4,5,8)
print(middle_no)
middle_no=middleNumber(8,2,1)
print(middle_no)
middle_no=middleNumber(8,2,9)
print(middle_no) 
middle_no=middleNumber(8,8,1)
print(middle_no) 

def divisibilityTest(middle_no:int)->int: 
    return middle_no%3==0 and middle_no%4==0 # This will return ture or false

print(divisibilityTest(middle_no))

#Method 2
def findMiddleNumber(num1: int, num2: int, num3: int) -> int:
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        return num1
    else:
        return num3


def isDivisibleBy3and4(number: int) -> bool:
    return number % 3 == 0 and number % 4 == 0  # This will directly return True/False


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))

middle_number: int = findMiddleNumber(num1, num2, num3)
print(f"The middle number is: {middle_number}")

if isDivisibleBy3and4(middle_number):
    print(f"{middle_number} is divisible by both 3 and 4.")
else:
    print(f"{middle_number} is not divisible by both 3 and 4.")



'''Q4. Write a Python program that takes four numbers from the user. 
Implement a function to find the average of the first three numbers.
Then, create another function to check if the average is greater than or equal to the fourth number.
Make sure to use these two functions to determine and 
'''


def calculateAverage(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3


def isAverageGreaterOrEqual(average: float, fourth_number: int) -> bool:
    return average >= fourth_number


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))
num4: int = int(input("Enter the fourth number: "))

average_value: float = calculateAverage(num1, num2, num3)

# Check if the average is greater than or equal to the fourth number
result = isAverageGreaterOrEqual(average_value, num4)

print(f"The average of {num1}, {num2}, and {num3} is: {average_value}")

if result:
    print(f"The average is greater than or equal to {num4}.")
else:
    print(f"The average is less than {num4}.")





