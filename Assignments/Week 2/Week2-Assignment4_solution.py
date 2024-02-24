'''Q1. Create a function named divs, which will take two parameters n1 and n2. 
Return the count of how many numbers from 1 to n1 are divisible by n2.'''

def divs(n1:int,n2:int):
    i=1 
    count=0
    while i<=n1: 
        if i%n2==0:
            count+=1
        i+=1
    return count    
    
count=(divs(10,2))
print(count)

'''Q2. From 1 to 2000, print all the LEAP YEARS, using WHILE loop.'''

def leap_years(num:int): 
    i=0
    while i<=num:
        if (i%4==0 and i%100!=0) or (i%400==0) : 
            print(i)
        i+=1

leap_years(2000)    

'''Q3. Create a function named factorial which takes a integer as an input and 
returns the factorial of that number.Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120'''

def factorial(num:int)->int: 
    i=num
    factorial_var=1
    while i>=1: 
        print(i)
        factorial_var=factorial_var*i
        i-=1
    print(factorial_var)  

factorial(5)      

'''Q4. Create a function named pattern which takes an integer as an input and print the following pattern.
10 20 30 40 50 60 70 80 100 110
'''

def patternTon(num:int): 
    i=1
    while i <=num: 
        print(i*10,end=' ')
        i+=1


patternTon(10)


'''Q6. Don’t create a function, just print the following pattern1  11  111  1111  11111....n times (Ask n from user)'''

n=int(input("Enter a Number= "))
i=1
sum=0
while i<=n: 
    sum=(sum+10**i)
    print(sum+1)
    i+=1

'''Q7. Keep asking numbers from user until the user enters 0. Then display the average of all numbers.
'''    

while True: 
    num=int(input("Enter the number="))
    if num==0: 
        break

'''Q8. Write a function named pattern which accepts an integer n as an argument. Then print the following pattern.
1,3,9,16,25,36,49,64
'''
def pattern_1(n:int):
    i=1
    sum=0
    while i<=n: 
        if i%2!=0:
            sum=sum+i
            print(sum)
        i+=1

pattern_1(20)


'''
Q9. Ask a number from user. Print if that number is prime or not, use functions.
'''

def primeNumbers(num:int):
    i=2
    while i<num: 
        if num%i!=0: 
            print(f"{num}:Prime Number")
            break
    i+=1  
    print(f"{num}:Not a Prime number")
         

primeNumbers(1)
primeNumbers(2)
primeNumbers(3)
primeNumbers(5)
primeNumbers(6)
primeNumbers(9)
primeNumbers(10)


'''Q10. Ask a number from user n1. From 1 to n1, print how many prime numbers are there.'''

def factorsCount(n: int) -> int:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def isPrime(n: int) -> bool:
    fc = factorsCount(n)
    if fc == 2:
        return True
    else:
        return False


i = 1
n1 = int(input("Enter a number = "))  # 15
count = 0
while i <= n1:
    if isPrime(i):
        count += 1
    i += 1

print(f"Total prime numbers between 1 to {n1} = {count}")