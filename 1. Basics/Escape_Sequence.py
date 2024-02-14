# Escape Sequence
"""\n: new line character 
\t : Tab
\\ : \
\" : "
\' : '
\ : backspace"""
print("My name is Ankita\nMy age is 28\nMy gender is female")

# Output: My name is My name is A\nkita
print(
    "My name is A\\nkita"
)  # double \\ to print \ once otherwise it would have been considered as new line

# Output: My name is A\\nkita
print(
    "My name is A\\\\nkita"
)  # double \\ to print \ once otherwise it would have been considered as new line and 4 time \\\\ to prin \\

# Output: My name is "Ankita"
print('My name is "Ankita"')
"""If we have to use double quotes "" inside the print as part of print then use single qoutes outside 
and it works vice versa to use single quotes inside prints then use "" double quotes out"""

# Output: My name is "Ankita"
print('My name is "Ankita"')  # Double quotes both inside and out

# Output: a"\\"xyz'"\
print('a"\\\\"xyz\'"\\')
