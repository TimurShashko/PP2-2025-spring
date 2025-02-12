import math
x = math.pi
degree = float(input("Input degree: "))
print("Output radian:", round((degree*x)/180, 6))
print("")

#2nd way
print(math.radians(degree))