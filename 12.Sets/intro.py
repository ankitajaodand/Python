''' Set stores unique element like keys are unique in dictionary, lists is like a list with unique values
1.defination : {55,67,33}
2. Unordered
3. mutable
4. To create empty set= set()
5. Sets values works as dictionary keys 
6. They are iterable by values like dictionary 
7. This is used since it's faster as compared list when we want to find a number is set
'''

a={33,33,33,45,'Ankita'} #while adding we can add duplicates however while priting it prints unique
print(a)

a = {33, 34, 11, 33, 33, 33, "ANirudh", "abc", 99.9}
b = {33, 12, 11, 9, 5, 6}
# print(a.union(b))
# print(a.intersection(b))
print(33 in a)
print(a)
for i in a:
    print(i)
# print(a)
# a.add(-100)
# a.remove(21)
# a.pop()
# print(a)