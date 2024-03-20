my_details = [
    {"name": "Anirudh", "age": 67, "gender": "Male"},
    {"name": "Clara", "age": 52, "gender": "Female"},
    {"name": "Vandana", "age": 63, "gender": "Female"},
    {"name": "Amber", "age": 23, "gender": "Male"},
]

def abc(fffff):
    return fffff["age"]

my_details.sort(key=abc, reverse=True)
print(my_details)
# my_details.sort(key=lambda z: z["age"], reverse=True)
# print(my_details)



students = {
    "anirudh": {"age": 66, "gender": "Male"},
    "sanjay": {"gender": "Male", "age": 32},
    "vandana": {"age": 53, "gender": "Female"},
}
print(students.items())
x = dict(sorted(students.items(), key=lambda x: x[1]["age"])) 
'''1.students.items returns list of tupples as below 
([('anirudh', {'age': 66, 'gender': 'Male'}), ('sanjay', {'gender': 'Male', 'age': 32}), ('vandana', {'age': 53, 'gender': 'Female'})])
2. sort traverse itself picks element by element so 1st element will be ('anirudh', {'age': 66, 'gender': 'Male'})
3. first element is a tupple is a tupple that can be sliced so we are using x[1]
3. second element in a tupple is dictionary which can not be sliced so x[1]["age"]
'''
print(x)
# print(x)


students = {
    "anirudh": {"age": 66, "gender": "Male", "marks": [2, 3, 11, 24, 55]},
    "sanjay": {"gender": "Male", "age": 32, "marks": [54, 76, 12, 232, 11, 65]},
    "vandana": {"age": 53, "gender": "Female", "marks": [65, 77, 33]},
}
print(students.items())
x = dict(sorted(students.items(), key=lambda x: sum(x[1]["marks"]))) #sum is a function can be used with any datatype



