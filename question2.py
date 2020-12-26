# 2. Даны действительные числа x и y.
# Получить (|x|-|y|)/(1+|xy|)

x = int(input("Введите первое число:"))
y = int(input("Введите первое число:"))
question = (abs(int(x)) - abs(int(y))/(1 + abs(int(x)*int(y))))
print("Ответ:" + " " + str(question))
