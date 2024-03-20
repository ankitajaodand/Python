
f=open("hello.txt","r")
print(f) #This returs object type and not the file
my_list=f.readlines()

for i in my_list:
   list1=i.split()[::-1]
   print(list1)
   print(" ".join(list1))
