'''Q4.
Write a Python function that takes two dictionaries as input, where the values are lists.
 The function should merge the lists corresponding to the same keys in both dictionaries 
 into a single list and return a new dictionary with these merged lists.'''

dict1 = {"x": [1, 2, 3], "y": [4, 5, 6],"a":[1,7]}
dict2 = {"x": [7, 8, 9], "y": [10, 11, 12], "z": [99, 100, 111]}

print(dict2.keys())
output_dict={}


for key,values in dict1.items(): 
    if key in dict2.keys():
        output_dict[key]=dict1[key]+ dict2[key]
    else : 
        output_dict[key]= dict1[key]   

for key,values in dict2.items(): 
    if key not in dict1.keys(): 
          output_dict[key]= dict2[key]  

print(output_dict)            


