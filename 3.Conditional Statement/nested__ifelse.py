''''
if C1:
    ------- 
    if c2: 
    --------
    -------
    else:
    -----
else:
--------
'''
'''
Ask Number from user and print positive negative zero
'''

num=int(input("Enter the num= "))

if num>=0: 
    if num>0: 
        print("Postive")
    else: 
        print("zero")
else:
    print("negative")   



"""
Ask a number from user.
Print Positive, Negative, Equal To Zero
"""
num = 67
# if num >= 0:
#     if num == 0:
#         print("Equal to zero")
#     else:
#         print("Positive")
# else:
#     print("Negative")
if num > 0:
    print("Positive")
else:
    if num == 0:
        print("Equal to zero")
    else:
        print("Negative")


"""
3 requirements to get a certificate
1. Should be a part of C&D
2. Minimum class attended should be 20
3. Minimum assignment submitted = 45

Are you part of C&D = yes
Enter class attendted = 56
Enter assignment submitted = 68
You are eligible for certificate
"""

part_cd= str(input("enter yes/no= ")).lower()
print(part_cd)

if part_cd=='yes': 
    no_class=int(input("enter no of classes attended= "))
    if no_class>=20:
        no_assi=int(input("enter no of assignments submitted= "))
        if no_assi>=45:
            no_assi=int(input("enter no of assignments submitted= "))
            print("You are eligible for certificate")
        else: 
            print("Not Eligible")
    else: 
            print("Not Eligible")   
else: 
    print("Not Eligible")        
        


