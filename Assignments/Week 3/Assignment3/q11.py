'''Q11. Create a function calculatePrime that accepts an List of Integers and print all the prime numbers in that list.'''

def calculatePrime(lst): 
    for i in lst:
        j=2
        while j<i: 
          if i%j==0: 
             print("Not a Prime No")
          else: 
             print("Prime No")
             break
          j+=1  


calculatePrime([5,7,8,9,11])
             
           




