import math

def multiply_list(numbers):
    return math.prod(numbers)

if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    result = multiply_list(nums)
    print("Список:", nums)
    print("Произведение всех чисел:", result)
