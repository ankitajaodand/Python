'''"""
Enter a = python
Enter b = good
pythongood

Enter a = 50
Enter b = 20
70
'''

a=input("enter the value1 ")

b=input("enter the value2 ")

if a.isdigit() and b.isdigit():
   result=int(a)+int(b)
else: 
    result=a+b   
print(result)


#Function
def add(string1:str,string2:str) :
    if string1.isdigit() and string1.isdigit():
        result=int(a)+int(b)
    else: 
        result=a+b   
    print(result)

a=input("enter the value1 ")

b=input("enter the value2 ")

add(a,b)



