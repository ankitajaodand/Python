''''
During the condition statements like this 
c1==c2==c3 in this case default it checks left to right
however it follows some rules like BODMAS it works by default
and if the operators are at same level then left to right
#Comparisons will be left to right
'''
print(2*2**5)# It will execute power first and then multiply
print(2*2**(5*2)) # It will execute bracket first

print(4 // 2 / 2)