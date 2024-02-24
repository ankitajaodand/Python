


def sum_of_no(n) -> int:
    sum: int = 0
    while n > 0:
        sum = sum + (n % 10)
        n = n // 10
    return sum

n: int = int(input("Enter the no"))

print(sum_of_no(n))