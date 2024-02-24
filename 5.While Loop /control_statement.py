'''Break or Continue
break : get out of the loop when you want to stop on specific condition specifically useful when you don't know the input size
continue: skip when you hit that specific condition and then continue executing the rest'''
 #to control the while loop
#Break
i=1
while i<=10: 
    print(i,end="")
    if i==5: 
        print()
        break 
    i+=1

# Ask input to user until he enter 0
    
sum=0
while True:
    num:int=int(input("Enter a Number: "))
    if num==0: 
        break
    sum+=num
print(sum)    










