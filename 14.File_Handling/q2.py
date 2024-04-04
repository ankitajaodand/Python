'''Method 2 for counting vowels'''
def count_vowels(filename): 
    sum=0
    f=open(filename)
    txt_read=f.read()
    print(txt_read)
    for i in txt_read: 
        if i in '123456789': 
            sum+=int(i)
    print(sum)


count_vowels('hello.txt')  
