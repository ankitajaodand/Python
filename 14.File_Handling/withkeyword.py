
'''With is used to auto close the file , its for clean up process same with can be used to connect/ diconnect data base'''

with open("hello.txt",'r') as f: 
    data=f.read()
    list=data.split() # file will remain open only within 'with'
print(list) #variables will be valid out of with with because data is stored in variable now 


#Method 1 to read from 1 file and write in another
with open("hello.txt", "r") as f1:
    data = f1.read()
    with open("hello1.txt", "w") as f2:
        f2.write(data)


#Method 2
with open("hello.txt", "r") as f1, open("hello1.txt", "w") as f2:
    f2.write(f1.read())