'''
Ask  Number from user and print positive negative zero
'''

num= int(input("Enter the num"))


#IF_ELIF_ELSE
'''If first if is true then it wont check elif'''
if num>0: 
    print("positive")

elif num<0:
   print(" negative")

else: 
    print("zero") 


#IF_IF_IF_ELSE 
''' It will check all the if's and print else also because else is for the last if
'''    


"""
Ask a number from. Print Positive, negative, equal to zero
"""
num: int = 52
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Equal to zero")

'''''
Ask Number, Yes if number is divisible by 5 and 6 
''''

num = int(input("Enter number = "))
if num % 5 == 0 and num % 6 == 0:
    print("Yes")
else:
    print("No")

'''
Ask a number from user. 
if div by 3 -> FOO
if div by 5 -> BAR
if div by both 3 and 5 -> FOOBAR
FOOFOOBARBAR
'''

num = int(input("Enter number = "))

if num % 5 ==0  and num % 3 ==0: 
    print("FOOBAR")
elif num % 3 == 0 :
    print("FOO")
elif num % 5 ==0 : 
    print("BAR")
else : 
    print("FOOFOOBARBAR")


''''

Ask a mark from user. 0-100
91-100 -> A
81-90 -> B
71-80 -> C
61-70 -> D
0-60 -> FAIL

'''   
mark= int(input("Enetr a number between 0-100= "))

if mark >= 91 and mark<=100 : 
    print("A")
elif mark >= 81 and mark<=90 : 
    print("B")
elif mark >= 71 and mark<=80 : 
    print("C")
elif mark >= 61 and mark<=70 : 
    print("D")
elif mark >= 0 and mark<=60 : 
    print("Fail")
else: 
    print("Invalid Marks, It should be between 0-100")        

    
"""
Rock Paper Scissors
computer_choice = rock/paper/scissors
user_choice = input() rock/paper/scissors
if
elif
elif

You won
You lost, the computer choose rock/paper/scissors
You tied
"""
import random
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = str(input("Enter rock/paper/scissors = ")).lower()
print(f"user_choice{user_choice}")

# IF-ELIF-ELIF

if user_choice not in options: 
    print("Invalid")
elif computer_choice==user_choice: 
    print("You tied")
elif computer_choice=='rock' and user_choice=='paper': 
    print("You won")  
elif computer_choice=='paper' and user_choice=='scissors': 
    print("You won")  
elif computer_choice=='scissors' and user_choice=='rock': 
    print("You won")
else: 
    print("you lost")     









