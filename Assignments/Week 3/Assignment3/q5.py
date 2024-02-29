'''Q5. Create a function countOddEven that accepts an List of Integers and print how many even and odd numbers are there'''

a5=[34,11,22,72,44,22,88]
odd_count:int=0
event_count:int=0


for i in range(0,len(a5)): 
    if a5[i]%2==0: 
        event_count+=1
    else: 
        odd_count+=1
print(f"even_count{event_count} \nodd count {odd_count}")


            


