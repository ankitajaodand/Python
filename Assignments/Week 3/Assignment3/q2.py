'''Q2. Make a list of your own. Print all the numbers divisible by 3 and 4 in that list.'''

a2=[1,2,3,4,5,6,7,12,16]

for i in range(0,len(a2)-1): 
    if a2[i]%3==0 and a2[i]%4==0: 
        print(f"{a2[i]} number is divisible by 3 and 4")





