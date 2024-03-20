'''To give the strict error for any condition
It is used when there is invalid input,so using assert stop the code execution
This can be achieved by if else also but it won't stop the code execution, it will print the error statement
We have write Assert as positive condition always whenever its true it will let code execute if it is false it will stop the code'''

# Assert
age = int(input("Enter your age = "))
assert age > 18, "You should be atleast 18 age" # if age is greater than 18 that is invalid input,so using assert stop the code execution
vote_id = int(input("Enter voting ID = "))
vote_id = input("Enter party to vote = ")


try:
    my_list = [54, 65, 78, 2, 123, 45, 65, 7, 11]
    index = int(input("Enter index number = "))
    assert index>=0 and index<len(my_list),"Index value is out of range" #This will be printed as ae in the exception
    print(my_list[index])
except AssertionError as ae:
    print(ae)
except:
    print("Unkonwn error")

