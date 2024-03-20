my_string="""HEllo world
This is Python 
We are doing good""" #This way comments will act like multiple line string

print(my_string)


#Tell the number of lines in file 

f=open("hello.txt","r")
print(f) #This returs object type and not the file
print(len(f.readlines()))
f.close()

#Print Number of Words

my_string="""HEllo world
This is Python 
We are doing good""" #This way comments will act like multiple line string

print(len(my_string.split())) #Splits by white spaces that includes \n or enter key

#Print Number of Words in each line
f = open("hello.txt", "r")

data=f.readlines()
for line in data:
    words=line.split()
    print(len(words))

f.close

#Print No of characters in each line
f=open("hello.txt","r")
print(f) #This returs object type and not the file
my_list=f.readlines()

for i in my_list:
    print(len(i.strip()))
f.close()

#Reverese Words in file 

f=open("hello.txt","r")
print(f) #This returs object type and not the file
my_list=f.readlines()

for i in my_list:
   list1=i.split()[::-1]
   print(list1)
   print(" ".join(list1))





