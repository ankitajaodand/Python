'''We can write it as an exception in cases of failure if you want to 
Mostly use in case of if else in the place of assertion  to indentify invalid input'''


try:
    age = int(input("Enter age = "))
    if age < 18:
        # raise ZeroDivisionError("Age cannot be less than 18")
        # raise IndexError("Age cannot be less than 18")
        raise Exception("Age cannot be less than 18")
    print("You can vote")
except Exception as e:
    print(type(e).__name__)
    print(e)