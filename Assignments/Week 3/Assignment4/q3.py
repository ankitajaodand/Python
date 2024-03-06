'''Q3. Write a Python function that takes two lists and returns True if they have at least one common element.'''

lst_1=[1,2,3.4]
lst_2=[5,6,1,9,10]

def commonElement(lst_1,lst_2):
    for i in range(0,len(lst_1)): 
        for j in range(0,len(lst_2)): 
            if lst_1[i]==lst_2[j]: 
                return True
                break 
    return False

lst_1=[1,2,3,4]
lst_2=[5,6,7,9,10]

ans=commonElement(lst_1,lst_2)
print(ans)
