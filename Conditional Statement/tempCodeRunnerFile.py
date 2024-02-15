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