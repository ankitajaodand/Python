'''Read from one file and write in another'''


input_file = input("Enter file to copy from = ")
output_file = input("Enter file to copy to = ")
f = open(input_file, "r")
data = f.read()
f.close()

f = open(output_file, "w")
f.write(data)
f.close()