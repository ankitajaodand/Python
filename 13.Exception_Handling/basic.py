'''
Python Error that's shown in terminal on code failure is divided in two parts 
1. Error Name 
2. Error Message 

Example : ZeroDivisionError: division by zero 
ZeroDivisionError : This is name of error
division by zero : This is message of an error 

Try ane Except block : if try is written except is mandatory 
It helps for smooth execution with faling

If Try except is wrotten, This exists running the try block if there is an error however it will still run the code outside try and except block

#else clause : Try and Excpet are the clauses that has else clause also 
else runs when there is no error

# Finally Clause : It runs in case of failure/sucess i.e it runs always. Finally clause can be used to disconnect the database 
In all the cases failure or success you have to disconnect the database.This can be used in the cleaning process as well

#Finally should be written as last after else clause



Types of Error 
1. zero divide by error 
2. value error 
3. index error 
4. Syntex error 
5. type error : because of Datatype'''


try: 
    print("Ankita")
    prim("Jaodand") #In normal case without exception handling it will fail at line 2 and 2 to 4 wont execute
    print("Python Class")
    print("Testing")
except : 
    print("Exception Handling: Unknown error") #Lines after failures wont run but code isn't stopped
finally: 
    print("This is Finally Clause")


try: 
    print("Ankita")
    print("Jaodand") #In normal case without exception handling it will fail at line 2 and 2 to 4 wont execute
    print("Python Class")
    print("Testing")
except : 
    print("Exception Handling: Unknown error") #Lines after failures wont run but code isn't stopped
else: 
    print("everything works fine")    #This will run only if there was no error in try block 
finally: 
    print("This is Finally Clause")    




