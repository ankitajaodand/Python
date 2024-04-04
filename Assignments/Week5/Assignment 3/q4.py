'''Q4. Write a Python program to Convert two lists into a dictionary
Sample Output
keys = ["One", "Two", "Three", "Four", "Five"] values = [1, 2, 3, 4, 5]'''

keys = ["One", "Two", "Three", "Four", "Five"] 
values = [1, 2, 3, 4, 5]
output={}

for index,value in enumerate(keys): 
    output[value]= values[index]

print(output)    



#Method 2

from typing import Dict, List


def convertToDictionary(lst1: List, lst2: List) -> Dict:
    dictionary = {}
    for i in range(len(lst1)):
        # dictionary.update({lst1[i]: lst2[i]})
        dictionary[lst1[i]] = lst2[i]
    return dictionary


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = convertToDictionary(keys, values)
print(my_dict)
