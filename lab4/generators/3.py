def div_by3n4(n):
    for divided in range(0, n + 1):
        if (divided % 4 == 0 and divided % 3 == 0):
            yield divided

n = int(input("Введите число до которого будут выводится числа кратные 3 и 4 одновременно, начиная с 0: "))

print(list(div_by3n4(n)))
