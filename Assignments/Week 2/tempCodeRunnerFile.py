def printPattern(number:int)->int:
    if number > 0:
        start = -number
        end = number
        while start <= end:
            print(start, end=" ")
            start += 1
    else:
        start = -number  # 20
        end = number  # -20
        while start >= end:
            print(start, end=" ")
            start -= 1   


number: int = int(input("Enter a number = "))  # -20  
printPattern(number)    