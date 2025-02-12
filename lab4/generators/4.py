def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("Введите начальное число: "))
b = int(input("Введите последнее число: "))

print(f"Квадраты чисел от {a} до {b}:")
for square in squares(a, b):
    print(square)
