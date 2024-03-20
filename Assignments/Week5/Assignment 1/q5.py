'''
Q5.
Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

#Without function
from typing import Dict
n=5
dict_output={}
for i in range(1,n+1) : 
    dict_output[i]=i*i 
print(dict_output)    



#   With Function
from typing import Dict


def createDictionary(n: int) -> Dict[int, int]:
    my_dict = {}
    for i in range(1, n + 1):
        my_dict[i] = i**2
    return my_dict


print(createDictionary(5))