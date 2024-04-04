'''Q5. Create a Python function to sort a dictionary by its values. And return that new dictionary.'''


Outputdictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


print(dict(sorted(Outputdictionary.items(),key= lambda x: x[1])))