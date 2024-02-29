'''Q3. Make a list of your own. Count how many numbers are divisible by 5.'''

a3=[1,3,2,6,9,10,12,20,30]
count=0

for i in range(0,len(a3)): 
    if a3[i]%5==0: 
        count+=1
print(count)



