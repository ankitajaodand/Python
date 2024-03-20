"""
Q1
anirudh has scored 432 marks
sanjay has scored 112 marks
Q2
anirudh has scored 87.44%
sanjay has scored 55.22%
"""
students = {
    "anirudh": {"physics": 54, "maths": 11, "english": 99},
    "sanjay": {"physics": 13, "maths": 40, "english": 62},
    "vandana": {"physics": 65, "maths": 85, "english": 94},
}

#Question 1


#Method 1 
"""
Q1
anirudh has scored 432 marks
sanjay has scored 112 marks
Q2
anirudh has scored 87.44%
sanjay has scored 55.22%
"""
students = {
    "anirudh": {"physics": 54, "maths": 11, "english": 99, "history": 43},
    "sanjay": {"physics": 13, "maths": 40},
    "vandana": {"physics": 65, "maths": 85, "english": 94},
}
for name, marks in students.items():
    total_marks = sum(marks.values())
    print(f"{name} has scored {total_marks} marks")


#Method2 
"""
Q1
anirudh has scored 432 marks
sanjay has scored 112 marks
Q2
anirudh has scored 87.44%
sanjay has scored 55.22%
"""

students = {
    "anirudh": {"physics": 54, "maths": 11, "english": 99, "history": 43},
    "sanjay": {"physics": 13, "maths": 40},
    "vandana": {"physics": 65, "maths": 85, "english": 94},
}



for name,marks in students.items(): 
    total_marks=0
    for j in marks.values(): 
      print(j)  
      print(total_marks)  
      total_marks=+j
    print(f"{name} has score {total_marks} marks")   
