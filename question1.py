#  1. Даны 2 действительных числа a и b.
#  Получить их сумму, разность и произведение.

a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
sum_ = int(a) + int(b)
print("Сумма:" + " " + str(sum_))

difference = abs(int(max(a, b)) - int(min(a, b)))
print("Разность:" + " " + str(difference))

product = int(a) * int(b)
print("Произведение:" + " " + str(product))
