'''Key Value pair
1.values can reapeat and keys can not
2.Datatypes of values can be different, it can be list as well another dict
3.keys can be imutable only int,float tupple,string.......it cannot be list since its mutable
4.values can be updated keys cannot
5.Dictornary can be extended with new key value pair,order will be maintained and newly added key will be added at the end
6. It is mutatable
7 to create empty dictionary 
    1. a={}
    2. b=dict() #this should be use so that we can differentiate it from set because set is also defined as {} without key value'''

my_dict={"Ankita": 28, "Anirudh":78}
print(my_dict)
print(type(my_dict))

#accessing dict
my_dict={"Ankita": 28, "Anirudh":78}
print(my_dict["Ankita"])


#Updating values

my_dict={"Ankita": 28, "Anirudh":78}
my_dict["Ankita"]=29
print(my_dict["Ankita"])

#Updates eixtsing key othwise adds
my_dict={"Ankita": 28, "Anirudh":78} 
my_dict["Nihar"]=45 
print(my_dict["Nihar"])

#Duplicate keys do not give error but it picks the last one when we call the key
my_dict={"Ankita": 28, "Anirudh":78,"Ankita":30} 
print(my_dict["Ankita"])