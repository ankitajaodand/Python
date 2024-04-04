'''Q8. Store name as a Key, and 5 marks in a List as a value in dictionary. 
Store details of at least 5 students. Print only the total marks of every student in ascending order.'''

students = [
    {"name": "Anirudh", "marks": [12, 43, 1, 76, 23]},
    {"name": "Akul", "marks": [78, 82, 80, 43, 62]},
    {"name": "Nihar", "marks": [13, 72, 32, 89, 53]},
    {"name": "Anusha", "marks": [43, 12, 79, 82, 85]},
    {"name": "Muskan", "marks": [54, 87, 72, 86, 84]},
]
marks=[]
for i in students: 
   marks.append(sum(i['marks']))
marks.sort()
print(marks)  

