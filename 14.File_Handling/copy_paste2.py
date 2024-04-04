import sys #sys.exit() use to exit the complete code execution, 
'''this is helpful in few cases since try except block won't stop code execution it will only stop execution of code in try block when error occurs'''


input_file = input("Enter file to copy from = ")
output_file = input("Enter file to copy to = ")
try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
except FileNotFoundError:
    print("File does not exists")
    sys.exit()
except:
    print("Some unknown error occurred")
    sys.exit()

try:
    f = open(output_file, "w")
    f.write(data)
    f.close()
except:
    print("Some unknown error occurred")
#...