def to_zero(n):
    for nums in range(n, -1, -1):
        yield nums

n = int(input("Введите число: "))

for num in to_zero(n):
    print(num)