'''count no of words in a file'''


def count_words(filename): 
    f=open(filename)
    txt_read=f.readlines()
    print(txt_read)
    count=0

    for i in txt_read: 
        for i in i.split() :  
            count+=1
    print(count)   

count_words('hello.txt')         

'''count vowels'''   
''''This is not correct, readlines gives list and read gives string, please follow method 2'''
def count_vowels(filename): 
    f=open(filename)
    txt_read=f.readlines()
    print(txt_read)
    count=0

    for i in txt_read: 
        for j in i.split() :  
            if j in ['a','e','i','o','u']:
                count+=1
    print(count)   

count_vowels('hello.txt')  


'''Method 2 for counting vowels'''
def count_vowels(filename): 
    count=0
    f=open(filename)
    txt_read=f.read()
    print(txt_read)
    for i in txt_read: 
        if i in 'aeiouAEIOU': 
            count+=1
    print(count)


count_vowels('hello.txt')  


   


