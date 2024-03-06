'''Q1. Make a list of your own. Make two more empty list like odd and even. Put all the even numbers from original list to even and odd numbers to 
odd and print both lists. (Don’t remove anything from original one)'''

from typing import List
def OddEven(lst:List[int]): 
    even=[]
    odd=[]
    for i in lst: 
        if i%2==0: 
            even.append(i)
        else: 
            odd.append(i)
    print(even)
    print(odd)


main_list=[1,2,3,4,5,6,7,8,9,10]
OddEven(main_list)





