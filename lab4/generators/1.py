def squares(n):
    for num in range(1, n + 1):
        yield num ** 2  

N = int(input("Введите число до которого будут выводиться квадраты чисел, начиная с 1: "))

squares_list = list(squares(N))

print(squares_list)
