#Strng 
'''
1. Immutable 
2. Almost same as list/tuple
'''


#1. Immutable 

#Exception 
a=''
print(id(a))
a+='xyz' #In this case ID is updated this a is recreated or overwritten and not muted 
print(id(a))
print(a)