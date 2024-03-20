
'''We can get values by keys but we cannot get not keys by values since values can be duplicate'''
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}

#Method 1
for i in my_dict:
    print(i) #Prints keys
    print(my_dict[i]) #To get key value
    print(i,my_dict[i]) #To get them together



#Method 2 
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
print(my_dict.keys())

for i in my_dict.keys():
    print(i,my_dict[i]) #To get them together

#Method 3 
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
print(my_dict.values())
for age in my_dict.values(): 
    print(age)

#method 4 Unpacking
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
print(my_dict.items())  #oustside list inside tupples
'''List of multiple tupples with key value can be converted to dict(list(tupples))'''

for i in my_dict.items():
    print(i) #prints k value pair in tupples

for i,v in my_dict.items(): #unpacking the 2 values in 2 variables
    print(i,v)    










