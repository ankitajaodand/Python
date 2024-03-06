'''Q5. Write a program to put all the common elements (in 2 lists) in another list and print it using function.'''

lst_1=[1,2,3,4,5,6,10,11]
lst_2=[1,2,3,4,5,6,7,8,9]
cmn_elements=[]

for i in lst_1: 
    if i in lst_2: 
        cmn_elements.append(i)
print(cmn_elements)