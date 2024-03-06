'''ASCII value numeric value behinde each character that CPU understands'''

a='a'

print(ord(a)) #ord prints ASCII value

'''ASCII USE CASE'''

'''Find count of e in the string'''
#This can be solved by other ways also below is solved by ASCII method 


a='ee'

count=0

for i  in a: 
    if ord('e')==ord(i): 
        count+=1
print(count)

''''''
