
'''Q8. Create a function findSmallest that accepts an List of Integers and returns the smallest number from the list.'''

def findSmallest(lst): 
    smallest=lst[0]
    for i in lst:
        if i<smallest: 
            smallest=i
    print(smallest)   


findSmallest([7,2,3,4,1,3])
