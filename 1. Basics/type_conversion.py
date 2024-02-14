'''
Type Conversion or Type Casting
To convert one data type in other
'''

#Output : Ankita Jaodand
a='Ankita'
b='Jaodand'
print(a+' '+b)


#Output : 300
a='100'
b='200'
print(a+b) #output 100200
print(int(a)+int(b)) #output 300

#Conversion to integer  
a='100.9' #float
print(int(a))#cannot be converted it will give value error since . is not the int 
a='100 '
print(int(a)) #this will work even if there is a space since it strips the spaces
print(int(10.0)) #100.9 was not working but 10.0 works
print(float(100)) #float to int is possible and outputs will be 100.00

#memory update if we convert the data type
a='123'
print(id(a))
b=int(a)
print(id(b))

#Float to int
print(int(55.95))# It will give output closer to floor 55 and not round off, decimal part will be removed
print(int(-5.56))# lowest integer closer to 0, value gets to nearest 0 

#Different datatypes to Boolean(Truthy or Falsy)
'''
Integer
Truthy: Everything except 0.00 is Truthy 1,2,3,4
Falsy : 0
String
String : Truthy:" ","abc" and everything and
Falsy: "" #without spaces inside
Float : 
Truthy: Everything except 0.00
Falsy : 0.00
'''
print(bool('abc'))
print(bool('0.10'))
print(bool(""))
print(bool(0))
print(bool(1))


