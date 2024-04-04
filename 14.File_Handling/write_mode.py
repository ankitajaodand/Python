'''Write the file
If file doesnt exists it creates otherwise it writes'''

f=open("anirudh.txt","w")
f.read() #This way it wont allow read since you open in write mode, you have to close and then reopen in read mode to read file
f.close()

f=open("anirudh.txt","w")
f.write("Hello Ankita") # 
f.write("How are you") # (There are 2 writes but it will write in the single line unless you give \n)
f.close()

f=open("anirudh.txt","w")
f.write("Hello Ankita\n") # 
f.write("How are you") # (There are 2 writes but it will write in the single line unless you give \n)
f.close()

'''If we close the file and reopen to write new lines, older lines will be deleted after closing, to handle this we have to use append instead 
of write'''