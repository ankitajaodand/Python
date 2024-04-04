'''Write a Python script to sort (ascending and descending) a dictionary by value.'''

dictionary = {1: 3, 3: 4, 4: 7, 2: 1, 0: 0}

print(dict(sorted(dictionary.items(),key=lambda x:x[1])))



from typing import Dict

def sortDictionary(dictionary: Dict, reverse=False):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(f"Ascending order = {sortDictionary(my_dict)}")
print(f"Descending order = {sortDictionary(my_dict,reverse=True)}")