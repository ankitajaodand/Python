def findMaximum(num1:int,num2:int,num3:int):
    if num1>= num2 and num1 >= num3:
        print(f"{num1} is Maximum") 
    elif num2>=num3: 
        print(f"{num2} is Maximum") 
    else: 
        print(f"{num3} is Maximum") 
    
findMaximum(10,11,13) 

