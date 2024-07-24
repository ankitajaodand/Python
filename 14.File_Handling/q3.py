'''Sum of numbers in sum_input.txt line by line'''

f=open('sum_input.txt')
data=f.readlines()
sum=0
for i in data: 
    sum+=int(i)
print(sum)    



import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
