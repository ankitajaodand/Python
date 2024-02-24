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