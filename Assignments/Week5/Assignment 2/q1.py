'''Q1.
Write a Python function that takes a dictionary as input where the values are lists.
The function should return a new list containing all the elements from all the lists in the dictionary.
It should have at least 3-4 keys and any amount of elements can be in a list.'''

from typing import Dict,List

iput_dict={'A':[1,2,3,4,5],'B':[6,7,8]}
output=[]
for key,value in iput_dict.items(): 
    for j in value: 
        output.append(j)
print(output)        



