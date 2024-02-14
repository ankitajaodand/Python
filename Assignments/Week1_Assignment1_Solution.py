
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




