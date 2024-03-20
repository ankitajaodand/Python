
a='delhi is a clean clean city'

r=a.replace("i","z")
print(r)

#without using replace


def replace(input_str: str)->str:
    result:str=str() #to create blank string
    for i in input_str:   
        if i.lower()=='i': 
            result+='z'
        else: 
            result+=i  
    print(result)   

replace('delhi is a clean clean city')  

#Comprehension and ternary 

my_str='delhi is a clean clean city'
lst_con=list(my_str)
updated_list=([ch if ch.lower()!='i' else 'z' for ch in lst_con])
result="".join(str(i) for i in updated_list)
print(result)


#using function 
def replaceChar(string: str) -> str:
    new_string: str = str()
    for char in string:
        if char.lower() == "i":
            new_string += "z"
        else:
            new_string += char
    return new_string

my_string: str = "delhi is clean city"
r = replaceChar(my_string)
print(r)


