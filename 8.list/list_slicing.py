#List Slicing 


# get 5 6 7 from my_lst to results
from typing import List

my_lst:List[int]=[1,2,5,6,7,9,1]

result=[]

for i in range(2,5):
    result.append(my_lst[i])
print(result)

#Same as above using slicing 
from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1]
result=my_lst[2:5]
print(result)

# Slice from index position 2 to last
from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1]
result=my_lst[2:] #default incrementer step is 1
print(result)
result=my_lst[2:len(my_lst)] #using length of my list
print(result)

# Slice from index position 2 to last with incrementar 2 
from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1]
result=my_lst[2::2]
print(result)
result=my_lst[2:len(my_lst):2] #using length of my list
print(result)
from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1,10,11,12,14] 
result=my_lst[2::4] #to count 4 consider zero'th element as first number printed and 4th numbet printed then 
print(result)

#Rervers Slicing
#Step decides the direction which is for positive left to right and negative moves from right to left with the mentioned step 
from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1,10,11,12,14] 
result=my_lst[::] #Default step is positive to negative left to right 
print(result)
from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1,10,11,12,14] 
result=my_lst[::-1] #to count 4 consider zero'th element as first number printed and 4th numbet printed then 
print(result)

from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1,10,11,12,14] 
result=my_lst[-4:-1] # Index is not given so it will only move left to right 
print(result)

from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1,10,11,12,14] 
result=my_lst[-1:-4] # Index is not given so it will only move left to right, so this will give empty result since -1 to -4 is not possible with positive step
print(result)

from typing import List
my_lst:List[int]=[1,2,5,6,7,9,1,10,11,12,14] 
result=my_lst[-1:-4:-1] # Index is not given so it will only move left to right, this will run with -ve step
print(result)








