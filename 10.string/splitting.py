my_string="Python is a great language"

result= my_string.split() #By default it splits by white space, white spaces means space,tab,\n

print(result)

#split by o

my_string="Aeroplane"

result= my_string.split('o') #When we split by o so there will not be o in the output, split by element is skipped

print(result)

# string 'python is great' reverse the string

my_list='python is great'

reverse_list=my_list.split()
reverse_list=reverse_list[::-1]

reverse_str=" ".join(str(i) for i in reverse_list)

print(reverse_str)

#Take input from user and reverse

my_list=str(input("enter the str"))

reverse_list=my_list.split()
reverse_list=reverse_list[::-1]

reverse_str=" ".join(str(i) for i in reverse_list)

print(reverse_str)

#
my_list=str(input("enter the str"))

my_list="python is great"
split_list=my_list.split()
result=[]
for i in split_list: 
    result.append(i[::-1])   
print(result)

result=" ".join(str(i) for i in result)
print(result)
