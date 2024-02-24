'''Ask number to user
number=10 then -10 to 10
number = 13 to 13
number=-13 then 13 to -13
'''

num:int=int(input("Enter number"))

if num>=0: 
    i=num-(num*2)
    while i<=num:
        print(i)
        i+=1
else: 
    i=num+(num*-2) 
    print("i is",i)
    while i>=num:#num=-10 and i=10
        print(i)
        i-=1

#Method 2 
num:int= int(input("Enter a number: "))

i: int = num*-1
j:int= num
if i <0: 
    while i<=num:
        print(i, end=" ")
        i += 1
    print()
else: 
    while j<=i:
        print(j, end=" ")
        j += 1
    print()

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
number: int = int(input("Enter a number = "))  # -20
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



