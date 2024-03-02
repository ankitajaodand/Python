'''Q6. Create a function sumCountOddEven that accepts an List of Integers '''



def sumCountOddEven(lst): 
    count_odd=0
    count_even=0
    for i in lst:
        if i%2==0:
            count_even+=1
        else: 
          count_odd+=1  
    print(f"Count of odd {count_odd}")
    print(f"Count of odd {count_even}")


sample_list=[1,2,3,4,5,6,7,8]

sumCountOddEven(sample_list)
        