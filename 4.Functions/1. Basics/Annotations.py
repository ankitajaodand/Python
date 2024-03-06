'''Helps to define the datatype of the variabale , not mandatory but to provide the information to the code user
If you v'''

a : int = 5
print(type(a))

a= 'Ankita' #This will also work since in python it is dymanic it decodes the datatype during run time 

a: int | float= 55 # This way a is expected to  be int or float 
print(a)

a: int = 5
print(a)
a = 432.3 
print(a)
b: int | float | str = 55
print(b)
b = 55.67
print(b)

r: int | float = 10 / 5

