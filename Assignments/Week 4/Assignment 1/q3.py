'''Q3. Make your own list of numbers. Ask a start and end position from User. Make another dierent list which will contain number from start to end position.
 Use slicing logic. (Same as previous question), but now print the result in reverse'''

def slicing(lst,start,end):
    print(lst[end:start-1:-1])


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
slicing(my_list, 2, 4)   
