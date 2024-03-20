'''Q3.
Write a Python function that takes a dictionary as input where the values are lists of integers. 
The function should return a new dictionary where the values are lists containing only the even integers from the original lists.'''


input_dict={'A':[1,2,3,4,5,6],'B':[7,8,10]}
output_dict=dict()
from typing import Dict,List


def filterDict(input_dict:Dict)-> Dict:
    for key,value in input_dict.items(): 
        input_list=[]
        for i in value: 
            if i%2==0: 
                input_list.append(i)
        output_dict[key]=input_list
    print(output_dict) 

filterDict(input_dict)

#Method 2
input_dict={'A':[1,2,3,4,5,6],'B':[7,8,10]}
filtered_dict = {}
for key, value in input_dict.items():  # Optimal Way
    filtered_dict[key] = [num for num in value if num%2==0 ]

print(filtered_dict)    

