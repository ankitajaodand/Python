'''
when you call the functions you don't follow the paratmeters sequence but pass it as variable_name=value
to pass the default values write in the function as variable_name:variable_type=0
If you default everything to 0 then you dont have to cumpulsory pass the arguments
'''


def totalMarks(
    physics: int, chemistry: int, maths: int, english: int = 0, computer: int = 0
): # english computer are not mandatory since they are defaulted to 0 already whatever are defaulted we define them last or right side
    print(f"{physics = }")
    print(f"{chemistry = }")
    print(f"{maths = }")
    print(f"{english = }")
    print(f"{computer = }")
    total = physics + chemistry + maths + english + computer
    print(f"Total marks = {total}")

totalMarks(english=54, physics=23, chemistry=78, computer=100, maths=78)
totalMarks(59, 100, english=34, computer=11, maths=98)
#totalMarks() #This will also run if all the marks are defaulted to 0 
totalMarks(45, 55, 85, computer=100)


def greet(name:str,age:int=0,gender:str ='not known'):
    print(f"name={name},age={age},gender={gender}")

greet('Ankita',age=28)