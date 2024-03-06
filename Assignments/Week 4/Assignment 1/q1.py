'''Q1. Make your own list of numbers. Ask a start and end position from User. 
Print the list from start position to end position using without using Slicing'''


def slicing(lst,start,end):
    result=[]
    for i in range(start,end+1): 
        result.append(lst[i])
    print(result)    


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
slicing(my_list, 2, 4)    

