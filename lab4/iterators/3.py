class squares:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()
    
    def next(self):
        while self.num <= self.n:
            if self.num % 3 == 0 and self.num % 4 == 0:
                cur = self.num
                self.num += 1
                return cur
            self.num += 1
        
        raise StopIteration()
    
N = int(input("Введите число до которого будут выводится числа кратные 3 и 4 одновременно, начиная с 0: "))
squares_list = list(squares(N))

print(squares_list)

