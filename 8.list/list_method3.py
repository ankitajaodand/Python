
'''Methods of list that we dont have to save anywhere just do variable.method()
updates is made in the variable itself'''

#Clear
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]

a.clear() #empties the list 
print(a)

#Pop : remove py index
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]
x=a.pop() #last element is removed from a and returned in x 
#print(a)
print(x)

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]
x=a.pop(-2) # element  at -2 is removed from a and returned in x : remove by index
#print(a)
print(x)

#remove : by value
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112,32]
a.remove('32') #remove value 32 and in case of duplicates it fist occurence
#print(a)
print(x)

#delete : this is not method of list this can be used for any variable 

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112,32]
del a 
print(id(a)) #doesnt exists since we have deleted 


#append
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112,32]
a.append([1,2,3,5])
print(a) #appends the complete list

#Extend : extend is iterable it takes as input list but adds the elements in the original list

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112,32]
a.extend([1,2,3,5])
print(a) 

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112,32]
a.extend([[1,2,3,5]]) #double [] to add the list 
print(a) 

#sort by default ascending 


a=[30,20,40,1,2,3,4,5,6,100,200]
a.sort() #changes in a itself
print(a)

#sort by default ascending for decending make reverse=True


a=[30,20,40,1,2,3,4,5,6,100,200]
a.sort(reverse=True) #changes in a itself
print(a)


