def solve(numheads, numlegs):
    for chickens in range (numheads + 1):
        rabbits = numheads - chickens
        total_legs = 2 * chickens + 4 * rabbits
        if total_legs == numlegs:
            return chickens, rabbits
    return None

print("Подсчет количества куриц и кроликов по общему количсетву голов и ног")

heads = int(input("Введите количество голов: "))
legs = int(input("Введите количество ног: "))

result = solve(heads, legs)

if result:
    chickens, rabbits = result
    print("Куриц: ", chickens, "Кроликов: ", rabbits)
else:
    print("Нет решения")