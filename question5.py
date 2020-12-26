# 5. Даны катеты прямоугольного треугольника.
# Найти его гипотенузу и площадь.

cathetus1 = int(input("Длина первого катета:"))
cathetus2 = int(input("Длина второго катета:"))
hypotenuse = ((cathetus1**2) + (cathetus2**2))**1/2
area = 1/2 * cathetus1 * cathetus2
print("Гипотенуза прямоугольного треугольника:", hypotenuse)
print("Площадь прямоугольного треугольника:", area)
