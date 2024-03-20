
#ReadLine
f=open("hello.txt","r")
print(f) #This returs object type and not the file
print(f.readline())  #This reads first line and since it has \n default at the end there will be one blank line
f.close()


#ReadLines '''This returns list of strings'''

f=open("hello.txt","r")
print(f) #This returs object type and not the file
print(f.readlines())
f.close()

f=open("hello.txt","r")
print(f) #This returs object type and not the file
print(f.readlines()[2]) #Third Line
f.close()

