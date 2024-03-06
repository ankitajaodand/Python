
my_list="python is great"
split_list=my_list.split()
result=[]
for i in split_list: 
    result.append(i[::-1])   
print(result)

result=" ".join(str(i) for i in result)
print(result)
