'''
Mandatory Steps: 
OPEN-->Close

Can be opened in 6 modes: 
text(t)(notepad,word,text) here t is default so we can ignore t it is just r,w,b instead of rt,wt,ar
1. Read(r)
2. Write(w)
3. Append(a)

binary(b)(ppt,img)
1. Read(rb)
2. Write(wb)
3. Append(ab)



'''

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

    

