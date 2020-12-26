# 4. Даны два действительных числа.
# Найти среднее арифметическое и среднее геометрическое этих чисел.

num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
listofnum = [num1, num2]
average = sum(listofnum)/len(listofnum)
geometricmean = (int(num1)*int(num2))**1/2
print("Среднее арифметическое:", str(average))
print("Среднее геометрическое:", str(geometricmean))
