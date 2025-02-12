class squares:
    def __init__(self, n):
        self.n = n
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()
    
    def next(self):
        if self.num <= self.n:
            cur, self.num = self.num**2, self.num + 1
            return cur
        raise StopIteration()
    
N = int(input("Введите число до которого будут выводится квадраты чисел, начиная с 1: "))
squares_list = list(squares(N))

print(squares_list)