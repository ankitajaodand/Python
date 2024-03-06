'''Q4. Write a Python Program to find sum and average of List in Python.'''


def sumAndAverage(lst): 
    sum=0
    average=0
    for i in lst: 
        sum+=i
    average=sum/len(lst)   
    print(f"sum:{sum}\naverage{average}") 


sumAndAverage([1,2])    