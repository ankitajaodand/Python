'''Q1. 2  22  222  2222  22222 ... upto n. (Ask n from user)'''

def pattern1(n:int)-> None: 
    i=0
    sum=2
    while i<=n: 
        sum=sum+(i*20)
        print(sum+i*10*20,end=' ')
        i+=1
        


n=int(input("Enter the number= "))
pattern1(5)

'''Q2. Write a program to display the n terms of a harmonic series and their sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n termsLets suppose n=5.
1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334'''