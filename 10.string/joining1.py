'''Replace all volwels with z'''

#Method 1
vowels=['a','e','i','o','u']
user_input=str(input("Please enter a str= "))
user_input=list(user_input)

my_list=['z' if i in vowels else i for i in user_input if i in user_input] # when we use ternary after for loop then it is when to add
print(my_list)

result="".join(str(i) for i in my_list) #converting to i 
print(result)

#Method 2 

vowels=['a','e','i','o','u']
user_input=str(input("Please enter a str= "))
user_input=list(user_input)

my_list=['z' if i in vowels else i for i in user_input if i in user_input] # when we use ternary after for loop then it is when to add
print(my_list)

result="".join(str(i) for i in my_list) #converting to i 
print(result)



