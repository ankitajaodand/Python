'''
Q1.
Make a dictionary with keys as subject name (physics, chemistry, etc.) and values as their marks. Print the highest marks scored.
'''


from typing import Dict

subject_marks: Dict[str, int] = {
    "physics": 67,
    "chemistry": 12,
    "english": 95,
    "computer": 99,
    "hindi": 54,
}
highest_mark=0
for key,value in subject_marks.items(): 
    if highest_mark<value: 
       highest_mark=value
print(f"Highest Mark {highest_mark}")       
    