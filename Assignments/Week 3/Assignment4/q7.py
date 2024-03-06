'''Q7. Make two lists of same length and pass it to a function. Return a third list where each element is the sum of index'''

a=[1,2,3,4,5]
b=[5,6,7,8,9]

def sumofIndex(lst1,lst2): 
    result=[]
    for i in range(0,len(lst1)): 
        result.append(lst1[i]+lst2[i])
    return result


a=[1,2,3,4,5]
b=[5,6,7,8,9]
x = sumofIndex(a,b)
print(x)

my_list1 = [43, 11, 92, 22]
my_list2 = [-100, -200, 221, 100]

x = sumofIndex(my_list1, my_list2)
print(x)