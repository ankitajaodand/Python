'''Q2. Write a function to remove duplicates from a list and print them.'''

from typing import List
def removeDuplicates(lst:List[int]): 
    common_integers=[]
    for i in lst: 
        if lst[i] not in common_integers: 
            common_integers.append(i)
    print(common_integers)
            
            
removeDuplicates([1,2,3,4,5,5,6,6])