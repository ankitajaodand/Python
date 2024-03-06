'''count the number of Captial letters'''

a='Python is a Coding Language'
count = 0
for i in a: 
    if ord(i) in range(ord('A'),ord('Z')+1) : 
        count+=1
print(count)        

    
#Method 2 
a = "PythOn is A GreAT LangAUGE"
count = 0
for char in a:
    ascii_number = ord(char)
    if ascii_number >= 65 and ascii_number <= 90:
        count += 1
print(count)


#Question 2 
'''count of number of digits'''
#Not the right method since spaces or any other character not in a to z is considered as number
a='python123'

count=0

for i in a: 
    if ord(i) not in range(ord('a'),ord('z')+1): 
        count+=1
print(count)


#Better Method 

a = "Pyth1On is A Gre3AT La1ngAU3 GE"
count = 0
for char in a:
    if "A" <= char <= "Z": #We can do directly this because in the background character A is ACII only
        count += 1
print(count)
# count = 0
# for char in a:
#     ascii_number = ord(char)
#     if ascii_number >= 65 and ascii_number <= 90:
#         count += 1
# print(count)