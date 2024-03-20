'''
Q3.
Make a dictionary with keys as subject name (physics, chemistry, etc.) 
and values as their marks. Print the name of the subject which has marks more than passing marks (above 33).
'''


from typing import Dict



subject_marks: Dict[str, int] = {
    "physics": 67,
    "chemistry": 12,
    "english": 95,
    "computer": 99,
    "hindi": 54,
}


for key,value in subject_marks.items():
    if value>33:
        print(f"{key}")