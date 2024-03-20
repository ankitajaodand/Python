
students={
    "Anirudh":{"age":66,"gender":'male'},
    "Vandana":{"age":30,"gender":'Female'},
    "Akul":{"age":10,"gender":'male'}
}

'''Anirudh has age 66
   Vandana has age 30
   Akul has age 10'''

for name,value in students.items(): 
    print(f"{name} has age value {value['age']}")   


#Method 2 this will resolve issue is age is not available   


students={
    "Anirudh":{"age":66,"gender":'male'},
    "Vandana":{"gender":'Female'},
    "Akul":{"age":10,"gender":'male'}
}

'''Anirudh has age 66
   Vandana has age 30
   Akul has age 10'''

for name,value in students.items(): 
    print(f"{name} has age value {value.get('age')}")   

    
