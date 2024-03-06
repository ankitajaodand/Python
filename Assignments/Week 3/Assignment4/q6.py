'''Q6. Write a program to remove the nth index element from a list using a function.'''

from typing import List


def removeNth(lst: List, n: int) -> None:
    if n<=len(lst)-1:
        lst.pop(n)
    else: 
        print("Index Does not exists")


my_list = [9008, 9102, 4311, 222, 98]
removeNth(my_list, 5)
print(my_list)