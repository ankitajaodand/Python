'''Q2. Make your own list of numbers. Ask a start and end position from User. 
Make another dierent list which will contain number from start to end position. Use slicing logic'''


def slicing(lst,start,end):
    print(lst[start:end+1])


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
slicing(my_list, 2, 4)   
