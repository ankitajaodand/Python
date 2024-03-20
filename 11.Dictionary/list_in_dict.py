'''"""
anirudh has scored 432 marks
sagar has scored 412 marks
"""
students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}'''

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}
for i, k in students.items():
    print(f"{i} has scored {sum(k)}")


for i, k in students.items():
    marks=0
    for j in k: 
        marks+=int(j)
    print(f"{i} has scored {marks}")        


#HomeWork 

"""
print average marks of each student 
print total marks of the class
print the max and min marks of every student
print the average marks scored by whole class
print the maximum mark in that class
"""
