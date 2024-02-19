#With parameters without retrun


def greet1(name:str,age:int,gender:str): 
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My gender is {gender}")


#greet() # This will be errored out since parameters are not passed

greet1('Ankita',28,'Femaile') # number of parameters should be equals to one defined in definations in this case there are 3

name=str(input("Enter name= "))
age=int(input("Enter name= "))
gender=str(input("Enter name= "))
greet1(name,age,gender)

# With Paramters, without Return

def greet(name: str, age: int, gender: str):
    name = ""
    age = 0
    gender = ""
    print(f"My Name is = {name}")
    print(f"My age is = {age}")
    print(f"My gender is = {gender}")

name = "Anirudh" 
age = 55
gender = "Male"
greet(name, age, gender) # these are called from functions so will be overwritten with blanks
print(name, age, gender) # this will print global variables so not overwritten


