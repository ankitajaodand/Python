'''Q3. Write a Python program to print a dictionary line by line.
Sample Output
Dict = {  "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89}, "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} }
WEEK 5 - ASSIGNMENT 3DICTIONARY SORTING AND MORE
info@codeanddebug.in Code and Debug codeanddebug.in
No need to submit anywhere, just keep track of all the PDF you made in a specific folder.
Compare your solution with the solution I’ll provide, in case of doubts, kindly reach out to me.
You may get assignment solution in format of PDF or VIDEO solution, depending on the diculty level.
'''

dict = {  "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89}, "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} }
for key,value in dict.items(): 
    print(key)
    for key2,value2 in value.items(): 
        print(f"{key2}:{value2}")

