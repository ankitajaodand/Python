'''
Input '''

a=input()
print("enter your name") #fraud it will take input first on the first line and then print this so use the method below
print("your name is {a}")

a=input("enter your name = ") #Input always returns string 
print("your name is {a}")

a=input("enter number1=")
b=input("enter number2=")
print(int(a)+float(b))


#Output
'''
Enter your name= Ankita
Enter your age= 28
Enter your gender= Female
'''
name=input("Enter your name= ")
age=input("Enter your age= ")
gender=input("Enter your gender= ")
print(f"My name is {name}\nMy age is {int(age)}\nMy gender is {gender}")