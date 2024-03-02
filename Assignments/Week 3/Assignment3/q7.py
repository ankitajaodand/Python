'''Q7. Create a function findLargest that accepts an List of Integers and returns the largest number from the list.'''


lst=[1,2,3,4,5,6,7]

def findLargest(lst):
    largest=0
    for i in lst:
        if largest<i:
            largest=i
    print(largest)

findLargest(lst)
