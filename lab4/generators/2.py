def even_numbers(n):
    for num in range(2, n, 2):
        yield num

n = int(input("Введите число: "))

even_numbers_str = ", ".join(str(num) for num in even_numbers(n))

print(even_numbers_str)
