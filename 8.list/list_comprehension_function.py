# List Comprehension and ternary using function 

def div(num): 
    if num%5==0 and num%4==0: 
        return True 
    else: 
        return False
    

my_list=[i for i in range(1,100) if div(i)==True]   
print(my_list) 



