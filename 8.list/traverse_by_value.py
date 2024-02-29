#traverse by value 
'''This needs to be used only when index of the list is not important
This doesn't need range since there is no index and index will be 0 to len(a)'''


a=[1,2,3,4,5,6,7,8,9,10]

sum=0
for i in a: 
    print(i)
    sum+=i
    print(sum)


#traverse using both index and value 
# enumerate provides both index and value
    
for index, value in enumerate(a) : 
     print(index,value)