f=open("hello.txt","r")
print(f) #This returs object type and not the file

#print(f.read())
data=f.read()
print(data)

f.close()


#looping
f=open("hello.txt","r")
for line in f: 
    print(line,end="")

for line in f: 
    print(line,end="") #File already has \n so we are using end to remove one more next line because print has default \n at the end to remove that use end=""

    
#Read Characters
f=open("hello.txt","r")
print(f) #This returs object type and not the file

print(f.read(3)) #reads first 3 characters from 0 to 2
print(f.read(5)) #This will read 5 characters after first 3, this is because it will have an imaginary cursor open until you close the file
f.close()

f=open("hello.txt","r")
print(f) #This returs object type and not the file
print(f.read()) 
print(f.read()) #this will print blank and not the data again because file is not closed after first print which has already read the entire data, this is again because of imaginary cursor
f.close()
