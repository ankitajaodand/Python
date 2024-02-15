
'''Q1. There are two variables.a=5b=10What will be the output of following:
'''
a=5
b=10
print(a > 5 and b >= 10)
print(a >= 5 or not b > 10)
print(not ( a > 5 and b > 5))
print(not ( a < 10 or not b < 10))
print(not ( not a <= 5 or not b >= 10))

'''Q2. Python program to convert kilometers to miles. Ask kilometer from User.'''

distance_kilo=input("Enter Distance in Kilometer= ")
distance_miles=0.621371* float(distance_kilo)
print(f"distance in miles {distance_miles}")


'''Q3. Ask 3 numbers from User and Calculate the Average.'''
a=int(input("Enter Number1= "))
b=int(input("Enter Number3= "))
c=int(input("Enter Number3= "))

avg=(a+b+c)/3
print(f"Average of 3 numbers is {avg}")

'''Q4. Ask value in Rupees and Convert into Paise.'''

rupees=float(input("Enter Rupees= "))
paise= rupees*100
print(f"rupees to paise {paise}")


'''Q5. Calculate Area of Square by taking side from User.'''
sq_side=float(input("Enter square side= "))
area_square=sq_side**2 #power 2
print(f"Area of square {area_square}")

'''Q6. Ask number of games played in a tournament. Ask the user number of games won and number of games loss. 
Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

'''
n_games=int(input("Enter Number of games in tournament= "))
n_lost=int(input("Enter number of games lost= "))
n_won=int(input("Enter number of games won= "))
n_ties=n_games-(n_lost+n_won)
print(f"Number of games got tie {n_ties}")
total_point=(4*n_won)+(2*n_ties)
print(f"Total Points {total_point}")