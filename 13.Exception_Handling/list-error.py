try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list[99])
    print(my_list[0] / my_list[-1])
except ZeroDivisionError:
    print("Cannot divide by zero, please check the values again")
except IndexError:
    print("Index is out of range")
except:
    print("Some unknown error occurred")


#With Else and Finally Clause

try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list)
    print(my_list[99])
    # print(my_list[0] / my_list[-1])
except ZeroDivisionError: #This runs in case of divide by zero error
    print("Cannot divide by zero, please check the values again")
except IndexError: #This runs in case of divide by index error
    print("Index is out of range")
except: #This Runs in any error except zerodivide or index since they are already defined above 
    print("Some unknown error occurred")
else: #This runs when there is no error
    print("Everything works fine")
finally: #This runs always
    print("This is a finally clause")

#To get the error message : 

try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list + "abc")
    # print(my_list[99])
    # print(my_list[0] / my_list[-1])
except ZeroDivisionError:
    print("Cannot divide by zero, please check the values again")
except IndexError:
    print("Index is out of range")
except Exception as e: #This helps to get the excpetion message for decoding
    print(e)
    print("Some unknown error occurred")

# To get the name of error message (type(error).__name__)

try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list + "abc")
    # print(my_list[99])
    # print(my_list[0] / my_list[-1])
except ZeroDivisionError:
    print("Cannot divide by zero, please check the values again")
except IndexError:
    print("Index is out of range")
except Exception as e: #This helps to get the excpetion message for decoding
    print(e) #This is message of the error
    print(type(e).__name__) #this is name of error
    print("Some unknown error occurred")

''' 
Error error exception needs to be written separtely because solution of all the errors will be different 
example in case of divide by error we may want to divide by 1
in case of type error will use type conversion 
however we don't know error then we dont knpw solution then it can be handled by except Exception as e

'''    