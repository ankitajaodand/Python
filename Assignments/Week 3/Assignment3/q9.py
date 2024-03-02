'''Q9. Create a function updateOddEven that accepts an List of Integers and update all the even numbers to 0
 and update all the odd numbers to 1.'''


def updateOddEven(lst):
    for index,value in enumerate(lst):
        if value%2==0:
            print(value) 
            lst[index]=0
        else: 
            lst[index]=1
    print(lst)

updateOddEven([1,2,3,4,5,6,7])