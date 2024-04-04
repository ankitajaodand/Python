with open("hello.txt",'r') as f: 
    data=f.read()
    list=data.split() # file will remain open only within 'with'
print(list)