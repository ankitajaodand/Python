'''Join is not possible with integers use only string'''

my_list=[1,2,3,4,5] # ints not possible in join so needs to be converted to str

result=" ".join(str( my_list)) #converting to i 

print(result)

result=" ".join(str(i) for i in my_list) #converting to i 

print(result)
