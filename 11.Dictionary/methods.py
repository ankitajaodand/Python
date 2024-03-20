



my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
#Clear
# my_dict.clear() #empties the dictionary
# print(my_dict)
# del my_dict #deletes the dictionary
# print(my_dict)
print(my_dict.get("Akul")) #same as slicing gets(my_dict['Akul']) the value of key Akul however if Akul is not present in error it returns None and not error like my_dict['Akul']
print(my_dict.get("Akul",100)) #By default it returns None but you want some thing else that can be defined after like 100
'''If key doesnt extis print the same '''

my_dict = {
    "anirudh": 78,
    "akul": 11,
    "muskan": 11,
    "sanjay": None,
}
keyname = input("Enter key name = ")

#Method 1 
'''This is no the correct way since key Sanjay has value as None So it will say doesn't exists'''
x = my_dict.get(keyname)
if x is not None:
    print(x)
else:
    print("Key does not exists")

#Method 1 
'''Solution to above issue'''
if keyname in my_dict:
    print(my_dict[keyname])
else:
    print("Key does not exists")


#Pop
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
x=my_dict.pop("Akul") #This removes the key and value of Akul 
print(x) #pop returns the value of key removed
print(my_dict)

#update
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
x=my_dict.update({"Akul":100,'vandana':25}) #This add new key value pair in the existing dictionary , it takes dictionary only, if already exists than updates/overwrites
print(my_dict)

#Copy 
my_dict={"Ankita": 28, "Anirudh":78,"Akul":10}
a=my_dict #This way Id's of my_dict and a is same so changes in one will cause changes in both
new_dict=my_dict.copy() #This creates copy at different ID 
print(new_dict)

#Copy creates the shallow copy that is ID of keys in both the dictionary is same 
my_dict={"Ankita": 28, "Anirudh":[78,10,55],"Akul":10}
new_dict=my_dict.copy()
print(id(my_dict)) #Id's of dictionaries of original and copy is same 
print(id(new_dict))
print(id(my_dict['Akul'])) #ID's of element will be different because copy creates shallow copy
print(id(new_dict['Akul'])) #ID's of element will be different because copy creates shallow copy

#deep copy this creates different ID's for the elements also 
my_dict={"Ankita": 28, "Anirudh":[78,10,55],"Akul":10}
new_dict=my_dict.deepcopy()
print(id(my_dict)) #Id's of dictionaries of original and copy is same 
print(id(new_dict))
print(id(my_dict['Akul'])) #ID's of element will be same because copy creates deep copy
print(id(new_dict['Akul'])) #ID's of element will be same because copy creates deep copy
