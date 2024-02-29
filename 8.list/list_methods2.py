

#id's will be same in case you copy variables this copies the memory or reference to save the memory
a=[1,2,3,4,5,6,7]
b=a

print(id(a))
print(id(b))


a=[1,2,3,4,5,6,7]
b=a
a.append(5) #append in a will also append in b since they points to same memory location
print(a)
print(b)


#Copy on different id's 
import copy
a=[1,2,3,4,5,6,7]
b=copy.copy(a) #this copies at different index
print(id(a))
print(id(b))
print(a)
print(b)
a.append(5) #this appends only in a and not in b since id's are different
print(a)
print(b)


#shallow copy
#id's of the elements in the list will be different, below is called as shallow copy where id of elements in the list is same 
import copy
a=[1,2,3,4,5,6,7]
print(id(a)) 
print(id(a[0]))

b=copy.copy(a)
print(id(b))  #id of a and b is same 
print(id(b[0])) #ids of the elements in a b will be same 

#deep copy 

import copy
a=[1,2,3,4,5,6,7]
print(id(a)) 
print(id(a[0]))

b=copy.deepcopy(a)
print(id(b))  #id of a and b is same 
print(id(b[0])) #ids of the elements in a b will different since we are doing deep copy

import copy
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]
b = copy.copy(a)  # Shallow Copy
b = copy.deepcopy(a)  # Deep Copy
print("A ->", a, id(a))
print("B ->", b, id(b))
b[3][1] = 1000
print("A ->", a, id(a))
print("B ->", b, id(b))


#copy without import, this is lists method called copy 


a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]
b =a.copy()  # Shallow Copy
print(id(a)) 
print(id(a[0]))
print(id(b))  #id of a and b is same 
print(id(b[0]))


