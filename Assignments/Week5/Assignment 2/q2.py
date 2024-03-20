'''Q2.
Create a function named countChar
which will accept a string as a parameter. Create a dictionary having frequency of each character'''

from typing import Dict
ouput_dict={}
def countChar(inpt_string:str) -> Dict: 
    dict_value=1
    for i in inpt_string: 
        ouput_dict[i]=dict_value
        dict_value+=1
    return  ouput_dict

print(countChar("hello"))       
